from django.shortcuts import render
import requests
import json 


def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e7e98c2c6ffd99bc079c09341ce82efd'
    city = 'hyderabad'


    
     

    response = requests.get(url.format(city)).json()
    print(response)

    city_weather = {
        'city':city,
        'temperature':response['main']['temp'],
        'description':response['weather'][0]['description'],
        'icon':       response['weather'][0]['icon'],

    }
    print(city_weather)

    context = {'city_weather': city_weather}
    print(context)

    
    return render(request, 'weather/test_weather.html', context)