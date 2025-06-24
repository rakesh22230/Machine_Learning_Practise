import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '105450e8bb58d41f8374b982b5c64934'  # Your OpenWeatherMap API key

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get('cod') != 200:
            messagebox.showerror("Error", data.get('message', 'Error fetching data'))
            return None

        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].title()
        }
        return weather
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data:\n{e}")
        return None

def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city)
    if weather:
        result = (
            f"City: {weather['city']}\n"
            f"Temperature: {weather['temperature']} °C\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Condition: {weather['description']}"
        )
        result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter city name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
