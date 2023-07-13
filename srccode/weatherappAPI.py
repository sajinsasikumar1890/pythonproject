import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Enter your OpenWeatherMap API key here
API_KEY = "your_api_key_here"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather', methods=['POST'])
def weather():
    # Get the city name from the user input
    city = request.form['city']

    # Send an API request to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract relevant weather data from the response
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]

    # Render the weather template with the weather data
    return render_template('weather.html', city=city, temperature=temperature, feels_like=feels_like, description=description)

if __name__ == '__main__':
    app.run(debug=True)
