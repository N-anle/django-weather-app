from django.shortcuts import render,get_object_or_404, redirect
import requests
from .forms import CityForm
from .models import City
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username already exists")
            return redirect ('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This Email already exists")
            return redirect ('signup')
        else: 
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            messages.success(request, "Your user was created successfully")
            return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('weather')
        else: 
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

@login_required
def weather(request):
    weather_data = []
    form = CityForm()

    if request.method == 'POST':

        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.user = request.user
            city.save()
            form = CityForm()

    cities = City.objects.filter(user=request.user)
        
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=1c2be5c11e6c2a06184fdff5b44e1b33&units=metric'

    for city in cities: 
        r = requests.get(url.format(city.name)).json()
        
        if r.get('main'):
            weather_info = {
                'city' : city,
                'temperature' :r['main']['temp'] ,
                'weather' : r['weather'][0]['main'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'] ,
            }
            weather_data.append(weather_info)
        else: 
            weather_info = {
                'city' : city,
                'temperature' :None,
                'weather' :"Data Unavailable",
                'description' : "Data Unavailable",
            }
            weather_data.append(weather_info)

    context = {
        'cities' : weather_data,
        'form' : form,

    }

    return render(request,'index.html',context)

@login_required
def delete(request, city_id):
    city = get_object_or_404(City,id = city_id)
    city.delete()
    return redirect('weather')

@login_required
def delete_all(request):
    City.objects.all().delete()
    return redirect('weather')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out Succesfully')
    return redirect('home')