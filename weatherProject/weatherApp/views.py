from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=3cec791d2cb0b8461afc34ee5db4f3eb').read()
        list_of_data = json.loads(source)

        data = {
            "id" : str(list_of_data['weather'][0]['id']),
            "country_code" : str(list_of_data['sys']['country']),
            "main" : str(list_of_data['weather'][0]['main']),
            "temp" : str(list_of_data['main']['temp']) + ' °C',
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
