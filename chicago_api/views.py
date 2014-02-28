from django.shortcuts import render
from django.http import HttpResponse
from social_data.models import Service, Post
from social_data import twitter

def home(request):
    # t = twitter.twitter()
    data_list = []
    for p in Post.objects.all():
        dictionary = {}
        dictionary['latitude'] = p.latitude
        dictionary['longitude'] = p.longitude
        dictionary['title'] = p.text
        dictionary['icon'] = p.service.icon
        data_list.append(dictionary)

    info = {
        'html_id':"map-canvas",
        'latitude': 41.8954,
        'longitude': -87.6243,
        'zoom': 10,
        'map_type': "ROADMAP",
        'm_data':data_list
    }
    return render(request, 'chicago_api/base.html', info)


