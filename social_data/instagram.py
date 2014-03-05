from social_data.models import Service, Post
from python_instagram import instagram
from datetime import datetime
from slistener import SListener
import time, sys

client_id='7fa959a59882475ba2231140f893bdf1'
client_secret='a7b40449a691447bb440add4141ac11e'
api = InstagramAPI(client_id = client_id, client_secret = client_secret)

def instagram():        
    l = api.location_search(distance = 5000, lat = "41.8954", lng =-"87.6243", count = 1000)
    s = Service.objects.get(name="instagram")
    for x in l:
        lat = x["latitude"]
        lon = x["longitude"]  
        find = Post.objects.filter(identifier = x.id, service = s)
        if len(find) == 0:
            post = Post(service = s, latitude = lat, longitude = lon, identifier = x.id, text = x.text, link = "", image = "", timestamp = x.created_at)
            #post.save()
            print("lat: " + lat + " long: " + lon)

    