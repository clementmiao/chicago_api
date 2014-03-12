from django.shortcuts import render
from django.http import HttpResponse
from social_data.models import Service, Post, Sentiment
from os import path

def home(request):
    BASE_DIR = path.dirname(__file__)
    rel_path = 'icons/doc.kml'
    # file_path = path.join(BASE_DIR, rel_path)
    file_path = rel_path
    data_list = []
    # s = Service.objects.get(name="twitter")
    # posts = Post.objects.filter(service= s )
    # for p in posts:
    #     dictionary = {}
    #     dictionary['latitude'] = p.latitude
    #     dictionary['longitude'] = p.longitude
    #     dictionary['title'] = p.text
    #     dictionary['icon'] = p.service.icon
    #     dictionary['image'] = p.image
    #     data_list.append(dictionary)

    sentiments = Sentiment.objects.all()
    for s in sentiments:
        dictionary = {}
        p = s.post
        dictionary['latitude'] = p.latitude
        dictionary['longitude'] = p.longitude
        dictionary['sentiment'] = s.sentiment
        data_list.append(dictionary)


    info = {
        'html_id':"map-canvas",
        'latitude': 41.8954,
        'longitude': -87.6243,
        'zoom': 10,
        'map_type': "ROADMAP",
        'm_data':data_list,
        'kml': file_path
    }
    return render(request, 'social_data/base.html', info)


