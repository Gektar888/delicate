import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    # appid = '12a5ccee7980adfc48c7c4416ab29c90'
    url = "https://chaturbate.com/api/public/affiliates/onlinerooms/?wm=0FJqU&client_ip=request_ip"
    results = 'username'
    res = requests.get(url).json()

    res1 = res['results']
    # username_info = {
    #     'username': results,
    #     'spoken_languages': res["results"][0]["spoken_languages"],
    #     'tags': res["results"][0]["tags"]
    # }
    context = {
        'info': res1
    }
    return render(request, 'weather/del.html', context)