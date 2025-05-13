from flask import Flask, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')  # 從環境變數取得 OpenWeatherMap API 金鑰

@app.route('/weather')
def weather():
    city = request.args.get('city', 'Taoyuan')
    lang = 'zh_tw'
    units = 'metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}&lang={lang}'

    res = requests.get(url)
    data = res.json()

    if res.status_code != 200 or 'weather' not in data:
        return f"找不到 {city} 的天氣資料。"

    description = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    reply = f"{city} 現在天氣：{description}，氣溫 {temp}°C，濕度 {humidity}%，風速 {wind_speed} m/s"
    return reply