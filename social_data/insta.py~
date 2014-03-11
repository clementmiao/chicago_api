from social_data.models import Service, Post
from instagram.client import InstagramAPI
#import get_access_token
from datetime import datetime
from slistener import SListener
import time, sys, math

client_id='7fa959a59882475ba2231140f893bdf1'
client_secret='a7b40449a691447bb440add4141ac11e'
access_token ='1124834969.7fa959a.49315f81b2e54d0e83c3dab81ff67794'
api = InstagramAPI(client_id = client_id, client_secret = client_secret)

#41.8954, -87.6243
def insta(la,lo):
    print("lat: " + str(la) + " log: " + str(lo))        
    l = api.media_search(distance = 5000, lat = la, lng =lo, access_token = access_token)
    s = Service.objects.get(name="instagram")
    for x in l:
        t = api.media(x.id)        
        #print(t.caption.text)
        lat =  t.location.point.latitude
        lon =  t.location.point.longitude
        #time = datetime.datetime.fromtimestamp(t.caption.created_time)  
        find = Post.objects.filter(identifier = x.id, service = s)
        if len(find) == 0:
            try:
                post = Post(service = s, latitude = lat, longitude = lon, identifier = t.id, text = t.caption.text, link = "", image = t.images['thumbnail'].url, timestamp = t.created_time)
                post.save()
            except Exception:
                pass
            
def move(lat, lon, radius):
    steps = int((round(radius/5000)))
    print(steps)
    for i in range(-1*steps,steps+1):
        for j in range(-1*steps,steps+1):
            print("i: " + str(i) + " j: " + str(j))
            #print(str(float((float(i)/float(steps))*radius/111000.0)) + " " + str(float((j/float(steps))*radius/85000.0)))
            insta(float(lat + (i/float(steps))*radius/111000.0),lon + float(float((j/float(steps))*radius/85000.0)))
