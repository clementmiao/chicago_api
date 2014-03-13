from social_data.models import Service, Post
from facepy import GraphAPI
from datetime import datetime, timedelta
import math
import webbrowser
import requests


app_id = "1491244067763247"
app_secret = "c4039a18ee0c2e4fd9da56f13454012e"

access_token="CAACEdEose0cBANb9UE4b7bwxUm4724FfjGwBpAKSCLWZCD4NPUZAVX\
			XWJZCqUq42OFAYDbeBMQNSYBZBf8j7Txk4SboqYu2sSNojZCZAP5J1M2g\
			PBDHrSC2dkWbuvEEhkyOaMLsZBE5VeZBjQz2bOh1arAbBWTUhdhcJLKFn\
			GwWUD50Qvw2Y7ihD7SMOmZCRlMyYNxYX3DZAad8AZDZD"





def facebook(lat,lon,radius):

	

	graph = GraphAPI(access_token)


	#Select ids of users who are friends with me, Sam Przezdziecki
	ids = graph.fql("SELECT uid2 FROM friend WHERE uid1 = me()")
	ids_data = ids['data']
	ids = []
	for n in range(len(ids_data)):
		ids.append(ids_data[n]['uid2'])

	#Pull geotagged posts 
	location_posts = []
	for num in ids:
		posts = graph.fql("SELECT latitude,longitude,id,message,\
							timestamp FROM location_post WHERE \
							author_uid = " + num)['data']
		if len(posts) != 0:
			location_posts.extend(posts)

	#Grab posts that are within 60 km of (41.8954,-87.6243) -- i.e., the center of Chicago
	filtered_posts = []
	for n in range(len(location_posts)):
		lat1 = location_posts[n]['latitude']
		lon1 = location_posts[n]['longitude']
		if(lat1 != None and lon1 != None):
			if (distance_in_km(float(lat1),float(lon1),lat,lon) < radius):
				filtered_posts.append(location_posts[n])
	
	#Save posts in database
	s = Service.objects.get(name="facebook")
	for x in filtered_posts:
		find = Post.objects.filter(identifier = x['id'], service = s)
		if len(find) == 0:
			d0 = datetime(1970,1,1)
			date = d0 + timedelta(seconds = x['timestamp'])
			post = Post(service = s, latitude = x['latitude'],\
				longitude = x['longitude'], identifier = x['id'],\
				 text = x['message'][:256], link = "", image= "",\
				  timestamp = date)
			post.save()
	print "Facebook scraped."




def distance_in_km(lat1,lon1,lat2,lon2):
	# Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = lon1*degrees_to_radians
    theta2 = lon2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    return arc * 6378.1 #radius of earth in km