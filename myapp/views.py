from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'True')
        appid = 'ADD_YOUR_WEATHER_API_HERE'
        api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, appid)
        # api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=7c054f05a1cdbb551ec3128b226a4d10'
        get_data = urllib.request.urlopen(api).read()   # get data of weather in JSON formt
        json_data = json.loads(get_data)    # bytes data convert into json
        x,y = json_data['coord']['lon'], json_data['coord']['lat'] 
        temprature = json_data['main']['temp']
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        visibility = json_data['visibility']
        country = json_data['sys']['country']
        cityName = json_data['name']
        context = {
            'x':x ,
            'y':y,
            'humidity':humidity,
            'pressure':pressure,
            'temprature':temprature, 
            'visibility':visibility,
            'country':country,
            'cityName':cityName
        }
        return render(request, 'index.html', {'context':context})
    else:
        return render(request, 'index.html')