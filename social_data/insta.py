from social_data.models import Service, Post
from instagram.client import InstagramAPI
#import get_access_token
from datetime import datetime
from slistener import SListener
import time, sys

client_id='7fa959a59882475ba2231140f893bdf1'
client_secret='a7b40449a691447bb440add4141ac11e'
access_token ='1124834969.7fa959a.49315f81b2e54d0e83c3dab81ff67794'
api = InstagramAPI(client_id = client_id, client_secret = client_secret)

def insta():  
    #popular_media = api.media_popular(count=20)
    #for media in popular_media:
     #   print media.images['standard_resolution'].url      
    l = api.media_search(distance = 5000, lat = 41.8954, lng =-87.6243, access_token = access_token)
    #print(l)
    s = Service.objects.get(name="instagram")
    for x in l:
        t = api.media(x.id)
        #print(t.caption)
        lat =  t.location.point.latitude
        lon =  t.location.point.longitude
        #time = datetime.datetime.fromtimestamp(t.caption.created_time)  
        find = Post.objects.filter(identifier = x.id, service = s)
        if len(find) == 0:
            post = Post(service = s, latitude = lat, longitude = lon, identifier = t.id, text = "", link = "", image = "", timestamp = t.created_time)
            #post.save()
            print(post)

    
