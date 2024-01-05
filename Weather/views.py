from django.shortcuts import render
import requests
import datetime
def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
        print(city)
    else :
        city='Dhaka'
        
    appid='6a172214d7364d519573c67e7f891734'
    URL='https://api.openweathermap.org/data/2.5/weather'
    PARAMS={
        'q':city,
        'appid':appid,
        'units':'metric',
        }
    r=requests.get(url=URL,params=PARAMS)
    res=r.json()
    # print(r)
    # sunset=res['sys']['sunset']
    # sunset_datetime = datetime.datetime.fromtimestamp(sunset)
    # print(sunset_datetime.strftime("%Y-%m-%d %H:%M:%S")) 
    
    context={
        'description':res['weather'][0]['description'],
        'icon':res['weather'][0]['icon'],
        'temp':res['main']['temp'],
        'feels_like':res['main']['feels_like'],
        'temp_min':res['main']['temp_min'],
        'temp_max':res['main']['temp_max'],
        'pressure':res['main']['pressure'],
        'humidity':res['main']['humidity'],
        'wind':res['wind']['speed'],
        'clouds':res['clouds']['all'],
        'city':city,
        'country':res['sys']['country'],
        
        
        }

    return render(request,'home.html',context)
