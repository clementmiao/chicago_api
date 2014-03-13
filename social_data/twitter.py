from social_data.models import Service, Post
import tweepy
import webbrowser
from datetime import datetime
from slistener import SListener
import time, sys

consumer_key='tAGy7M2xyAfDxYo0dpWW3Q'
consumer_secret='4fc51bhC3ero5Mj3WKnME6QT698ze9KRPPPh4lqI'
#access_token_key='2282396101-ij3EpglESz2RCj7dYqlNkbFap520PPy6hOgBLwR'
#access_token_secret='kOgg3N9hgWxLigi9yfIoShqrn6l3kgyvRDOiK8chtnC2M'
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token_key, access_token_secret)
#api = tweepy.API(auth)

def twitter(lat,lon,radius): #lat,lon floats; radius in kms
        print "Hi! We are going to redirect you to an authorization site."
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'
            return

        webbrowser.open(redirect_url)
        pin = raw_input("Enter the pin:")
        try:
            access_token = auth.get_access_token(pin)
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'
            return
        access_token_key = access_token.key
        access_token_secret = access_token.secret

        auth.set_access_token(access_token_key,access_token_secret)
        api = tweepy.API(auth)
        print "You are authorized! How many times would you like to scrape twitter?"
        num_scrapes_string = raw_input(">")
        num_scrapes = int(num_scrapes_string)
        i = 0
        while i < num_scrapes:
            l = api.search(geocode = "%d,%d,%dkm" %(lat,lon,radius), count = 10000)
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
            i += 1
            # print "Done for now"

    