from social_data.models import Service, Post
from instagram.client import InstagramAPI
from datetime import datetime
from slistener import SListener
import time, sys, math

client_id='7fa959a59882475ba2231140f893bdf1'
client_secret='a7b40449a691447bb440add4141ac11e'
access_token ='1124834969.7fa959a.49315f81b2e54d0e83c3dab81ff67794'
api = InstagramAPI(client_id = client_id, client_secret = client_secret)

#41.8954, -87.6243, Downtown Chicago Latitude and Longitude

#Finds and stores in the database instagram posts within a 5 km radius of point passed in
def insta(la,lo):        
    l = api.media_search(distance = 5000, lat = la, lng =lo, access_token = access_token) # Get data from Instagram
    s = Service.objects.get(name="instagram")
    for x in l: #pull relevent data
        t = api.media(x.id)        
        lat =  t.location.point.latitude
        lon =  t.location.point.longitude  
        find = Post.objects.filter(identifier = x.id, service = s) # check to see if we have this in our database already
        if len(find) == 0: # if not, then add it to the database
            try:
                post = Post(service = s, latitude = lat, longitude = lon, identifier = t.id, text = t.caption.text, link = "", image = t.images['thumbnail'].url, timestamp = t.created_time)
                post.save()
            except Exception:
                pass

##Because the instagram search function only allows for a 5 km radius for searching, 
#for anything bigger than this we need to call the function multiple times and make overlapping circles 
#takes a lattitude, longitude, and a radius in meters           
def move(lat, lon, radius):
    steps = int((round(radius/5000))) #number of calls in each direction to get the desired radius
    for i in range(-1*steps,steps+1):
        for j in range(-1*steps,steps+1):
            insta(float(lat + (i/float(steps))*radius/111000.0),lon + float(float((j/float(steps))*radius/85000.0)))
