import requests
import json
import cv2
import numpy as np 
import pytesseract as pt 
import imutils

api_key = "e057598041c0ad8660a84900a6672f86"

city_name = input("Enter city name : ")

complete_url = "https://api.openweathermap.org/data/2.5/weather" + "?appid=" + api_key + "&q=" + city_name + "&units=metric"

response = requests.get(complete_url)
if response.status_code == 200:
    data = response.json()
    vreme = data['weather'][0]['description']
    temperature = round (data["main"]["temp"],2)
    wind_speed = data["wind"]["speed"] 
    humidity = data["main"]["humidity"]
    f = open("output_vreme.txt", "w")
    f.write("Vremea: " + str(vreme) + "\n")
    f.write("Temperatura: " + str(temperature) + "\n")
    f.write("Viteza vantului: " + str(wind_speed) + "\n")
    f.write("Humiditate: " + str(humidity) + "\n")

else:
    print(" City Not Found ")

