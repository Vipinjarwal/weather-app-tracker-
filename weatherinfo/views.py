from django.shortcuts import render
import requests
import datetime
import pytz
from .models import HistoricalData
import json
from django.contrib.auth.decorators import login_required


ist = pytz.timezone("Asia/Kolkata")


@login_required(login_url="/login/")
def home(request):
    api_key = "009f00a3864129f06bd2260886bd0b63"
    city_name = request.GET.get("city")
    current_datetime = datetime.datetime.now()

    if request.GET.get("city") == "":
        return render(request, "index.html", {"error": True})

    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    ).json()

    cod = data.get("cod")
    if cod == 200:
        fetch_data = {
            # 'cod': data.get('cod'),
            "city": data.get("name"),
            "country": data["sys"].get("country"),
            "weather": data["weather"][0].get("main"),
            "description": data["weather"][0].get("description"),
            "icon": data["weather"][0].get("icon"),
            "kelvin_temperature": data["main"].get("temp"),
            "celsius_temperature": int(data["main"].get("temp", 273.15) - 273.15),
            "pressure": data["main"].get("pressure"),
            "humidity": data["main"].get("humidity"),
            "wind": data["wind"].get("speed"),
            "sunrise": data["sys"].get("sunrise"),
            "sunset": data["sys"].get("sunset"),
            "current_datetime": current_datetime,
        }

        # Convert sunrise and sunset timestamps to formatted strings
        fetch_data["sunrise_formatted"] = datetime.datetime.fromtimestamp(
            fetch_data["sunrise"], ist
        ).strftime("%Y-%m-%d %H:%M:%S")
        fetch_data["sunset_formatted"] = datetime.datetime.fromtimestamp(
            fetch_data["sunset"], ist
        ).strftime("%Y-%m-%d %H:%M:%S")

        context = {"data": fetch_data}
        return render(request, "index.html", context)
    else:
        context = {"msg": f"{city_name} is not vaild location", "cod": cod}
        return render(request, "index.html", context)


@login_required(login_url="/login/")
def historical(request):
    if request.method == "GET":
        city_name = request.GET.get("city")
        print(city_name)
        data = HistoricalData.objects.filter(city_name=city_name)
        print(data)
        context = {"data": data}
        print(context)
        return render(request, "historical.html", context)
    else:
        context = {"msg": f"{city_name} is not vaild location"}
        return render(request, "historical.html", context)


def service(request):
    return render(request, "service.html")


def question(request):
    return render(request, "question.html")


def contact(request):
    return render(request, "contact.html")


def contactform(request):
    return render(request, "contactform.html")


def contact(request):
    return render(request, "contact.html")


# def historical_data(request):
#     json_file_path = (
#         "D:\Python-Main-Project\weather-tracker\WeatherTracker\historical_data.json"
#     )

#     # Read the JSON file with explicit encoding
#     # Read the JSON file with explicit encoding
#     with open(json_file_path, "r", encoding="utf-8") as json_file:
#         data_list = json_file.readlines()
#     # Iterate through the JSON objects and create HistoricalData objects
#     for json_data in data_list:
#         try:
#             data = json.loads(json_data)
#             print("Loaded")
#         except json.JSONDecodeError:
#             # Handle invalid JSON data (e.g., empty lines)
#             print("skipped")
#             continue
#         data["time"] = datetime.datetime.fromtimestamp(data["time"], ist).strftime(
#             "%Y-%m-%d %H:%M:%S"
#         )
#         HistoricalData.objects.create(
#             city_id=data["city"]["id"],
#             city_name=data["city"]["name"],
#             findname=data["city"]["findname"],
#             country=data["city"]["country"],
#             lon=data["city"]["coord"]["lon"],
#             lat=data["city"]["coord"]["lat"],
#             time=data["time"],
#             temp=data["main"]["temp"],
#             pressure=data["main"]["pressure"],
#             humidity=data["main"]["humidity"],
#             temp_min=data["main"]["temp_min"],
#             temp_max=data["main"]["temp_max"],
#             wind_speed=data["wind"]["speed"],
#             clouds_all=data["clouds"]["all"],
#             weather_id=data["weather"][0]["id"],
#             weather_main=data["weather"][0]["main"],
#             weather_description=data["weather"][0]["description"],
#             weather_icon=data["weather"][0]["icon"],
#         )

#     print("Data imported successfully")
