from django.shortcuts import render
import requests


def Home(request):
    key = "<api key>"
    url = "http://api.weatherapi.com/v1/current.json?key={}&q={},{}&aqi=no"

    if request.method == "POST":
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]

        try:
            result = requests.get(url.format(key, latitude, longitude)).json()

        except:
            print("try again")

        context = {
            "latitude": latitude,
            "longitude": longitude,
            "location": result["location"]["name"],
            "condition_text": result["current"]["condition"]["text"],
            "condition_icon": result["current"]["condition"]["icon"],
            "humidity": result["current"]["humidity"],
            "time": result["location"]["localtime"],
            "temp": result["current"]["temp_c"],
            "feels_like": result["current"]["feelslike_c"],
            "uv": result["current"]["uv"],
        }
    else:
        context = {}

    return render(request, "index.html", context)
