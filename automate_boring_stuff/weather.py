from pathlib import Path
import requests, json

city_name = '----------'
API_key = '--------'

current = requests.get(f"https://api.weatherstack.com/current?access_key={API_key}&query={city_name}")
current_data = current.json()

'''forecast = requests.get(f"https://api.weatherstack.com/forecast?access_key={API_key}&query={city_name}&forecast_days=1&hourly=1")
forecast_data = forecast.json(forecast.text)'''

path = Path('current_weather.json')
content = json.dumps(current_data)
path.write_text(content)