from social_data.models import Service, Post
import tweepy
from datetime import datetime
from slistener import SListener
import time, sys

consumer_key='fEwVGrkUxSaynSoQlZSEw'
consumer_secret='EPorM8IdsG59meK5HVB80ADb6kdCkIuBWtGim5uDogc'
access_token_key='2282396101-ij3EpglESz2RCj7dYqlNkbFap520PPy6hOgBLwR'
access_token_secret='kOgg3N9hgWxLigi9yfIoShqrn6l3kgyvRDOiK8chtnC2M'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

def twitter():
        # print "Hello Bob"
        
        
        l = api.search(geocode = "41.8954,-87.6243,60km", rpp = 10000)
        # list = api.home_timeline()
        s = Service.objects.get(name="twitter")
        for x in l:
            if x.geo != None:
                lat = x.geo["coordinates"][0]
                lon = x.geo["coordinates"][1]  
                find = Post.objects.filter(identifier = x.id, service = s)
                if len(find) == 0:
                    post = Post(service = s, latitude = lat, longitude = lon, identifier = x.id, text = x.text, link = "", image = "", timestamp = x.created_at)
                    post.save()
        # print "Done for now"

# def listen():
#     track = 
    