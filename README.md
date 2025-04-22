# Django Weather Checker App

A simple Django web application that allows users to sign up, log in, add cities, and check the current weather for those cities using the OpenWeatherMap API.

## Features

* **User Authentication:**
    * User Signup
    * User Login
    * User Logout
* **Weather Tracking:**
    * Add cities to track weather.
    * View current temperature, weather condition, description, and icon for added cities.
    * Delete individual cities.
    * Delete all tracked cities for the logged-in user.
* **Personalized Experience:** Each user manages their own list of cities.
* **Messaging:** Provides feedback to the user (e.g., successful signup, login errors, successful logout).

## Technology Stack

* **Backend:** Django (Python Web Framework)
* **Frontend:** HTML (using Django Templates)
* **API:** [OpenWeatherMap API](https://openweathermap.org/api) for weather data
* **Database:** Default Django SQLite (or configurable in `settings.py`)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # Make sure you have Django and requests in your requirements.txt
    # Example requirements.txt:
    # Django>=3.0
    # requests
    ```

4.  **Get an OpenWeatherMap API Key:**
    * Sign up on [OpenWeatherMap](https://openweathermap.org/appid) to get a free API key.
    * **Important:** The provided code has the API key hardcoded in `views.py`. It's highly recommended to store this securely, for example, using environment variables or Django settings.
        * Replace `'1c2be5c11e6c2a06184fdff5b44e1b33'` in the `weather` view within `views.py` with your actual API key (or preferably, load it from settings/environment).

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  **Navigate** to the application homepage.
2.  **Sign up** for a new account or **Log in** if you already have one.
3.  Once logged in, you'll be redirected to the **weather page**.
4.  **Enter a city name** in the input field and click "Add City".
5.  The weather information for the added city will be displayed.
6.  You can **add multiple cities**.
7.  Use the **delete buttons** next to each city or the "Delete All" button to remove cities from your list.
8.  **Log out** when finished.

## File Structure Overview (Relevant Files)

weather-api/|-- weather/|   |-- migrations/|   |-- init.py|   |-- admin.py|   |-- apps.py|   |-- forms.py       # Contains the CityForm|   |-- models.py      # Contains the City model|   |-- tests.py|   |-- urls.py        # App-specific URLs (you'll need to create this and include it in the project urls.py)|   |-- views.py       # Contains the view logic (signup, login, weather, delete, etc.)|-- templates/         # Directory for HTML templates|   |-- home.html|   |-- signup.html|   |-- login.html|   |-- index.html     # Weather display page|-- your_project_name/|   |-- init.py|   |-- asgi.py|   |-- settings.py    # Project settings (database, installed apps, etc.)|   |-- urls.py        # Project-level URLs|   |-- wsgi.py|-- manage.py          # Django management script|-- requirements.txt   # Project dependencies|-- README.md        

