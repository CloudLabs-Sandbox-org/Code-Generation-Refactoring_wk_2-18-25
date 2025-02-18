import requests
import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

# Create input field and button
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

city_entry = ttk.Entry(input_frame)
city_entry.insert(0, "London")
city_entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(input_frame, text="Search")
search_button.pack(side=tk.LEFT)

# Create labels for displaying weather info
city_label = ttk.Label(root, text="", font=('Helvetica', 14, 'bold'))
temp_label = ttk.Label(root, text="")
temp_f_label = ttk.Label(root, text="")  # New label for Fahrenheit
humidity_label = ttk.Label(root, text="")
desc_label = ttk.Label(root, text="")

# Position labels
city_label.pack(pady=10)
temp_label.pack(pady=5)
temp_f_label.pack(pady=5)  # Pack the new Fahrenheit label
humidity_label.pack(pady=5)
desc_label.pack(pady=5)

# OpenWeatherMap API configuration
API_KEY = '939685597c5488b0301576376e2c6836'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def update_weather():
    city = city_entry.get()
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        # Update labels with weather data
        temp_c = weather_data['main']['temp']
        temp_f = (temp_c * 9/5) + 32  # Convert Celsius to Fahrenheit
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        
        city_label.config(text=f"Weather in {city}")
        temp_label.config(text=f"Temperature: {temp_c:.1f}°C")
        temp_f_label.config(text=f"Temperature: {temp_f:.1f}°F")
        humidity_label.config(text=f"Humidity: {humidity}%")
        desc_label.config(text=f"Conditions: {description}")
        
    except requests.exceptions.RequestException as e:
        city_label.config(text="Error")
        temp_label.config(text=f"Could not fetch weather data: {e}")

# Configure button command
search_button.config(command=update_weather)

# Initial weather update
update_weather()

# Start the GUI event loop
root.mainloop()