import os
import json
import urllib.request
import urllib.parse
import urllib.error
# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request, abort
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def tocelcius(temp):
    # Standard Kelvin to Celsius subtraction is -273.15
    return str(round(float(temp) - 273.15, 2))

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # Default city is Mathura
        city = 'mathura'

    # Retrieve OpenWeatherMap API key from environment variables with fallback
    api_key = os.environ.get('OPENWEATHER_API_KEY')

    try:
        # Safely encode the city name for query parameters
        encoded_city = urllib.parse.quote(city)
        # Using secure HTTPS protocol
        url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}"
        
        with urllib.request.urlopen(url) as response:
            source = response.read()
        
        list_of_data = json.loads(source)

        return render_template(
            'index.html',
            city_name=city.title(),
            country=list_of_data['sys']['country'],
            coord_lon=list_of_data['coord']['lon'],
            coord_lat=list_of_data['coord']['lat'],
            temp_kelvin=round(float(list_of_data['main']['temp']), 2),
            temp_celsius=tocelcius(list_of_data['main']['temp']),
            pressure=list_of_data['main']['pressure'],
            humidity=list_of_data['main']['humidity'],
            error=None
        )
    except urllib.error.HTTPError as e:
        if e.code == 404:
            error_msg = f"City '{city}' not found. Please check spelling."
        elif e.code == 401:
            error_msg = "Invalid API key. Please check your OpenWeatherMap API configuration."
        else:
            error_msg = f"OpenWeatherMap API error: HTTP {e.code}."
        return render_template('index.html', error=error_msg)
    except urllib.error.URLError as e:
        return render_template('index.html', error="Failed to connect to the weather service. Please check your network connection.")
    except Exception as e:
        return render_template('index.html', error="An unexpected error occurred while fetching weather data.")

if __name__ == '__main__':
    app.run(debug=True)

