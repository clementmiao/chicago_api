from social_data.models import Service, Post
from facepy import GraphAPI
from datetime import datetime, timedelta
import math


app_id = "1491244067763247"
app_secret = "c4039a18ee0c2e4fd9da56f13454012e"

# CANNOT BE HARDCODED.
access_token = "CAACEdEose0cBABX5vI1qIpNTBSb0z2i6mzxJBWDZCrTe6Y9k44nAX5w1ip1\
				EMz8bvDqV2fnoGclRvtADvxHSmhxdQNn8kjidpgAOzuUxfOycZBrfLw8KdQ0\
				ppvNme8f8kCCU6rQdI5AIBPhZA2Bde7V0jL9FZBluXkCVwSZCzYWWQZBrUBw\
				994bQzZB2BBnQpFILbY3FbkJFgZDZD"

graph = GraphAPI(access_token)




def scrape_facebook():

	#Select ids of users who are friends with me
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

	#Grab posts that are within 60 km of (41.8954,-87.6243)
	filtered_posts = []
	for n in range(len(location_posts)):
		lat1 = location_posts[n]['latitude']
		lon1 = location_posts[n]['longitude']
		if(lat1 != None and lon1 != None):
			if (distance_in_km(float(lat1),float(lon1),41.8954,-87.6243) < 60):
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