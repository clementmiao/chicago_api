from social_data.models import Service, Post
from instagram.client import InstagramAPI
# import get_access_token
from datetime import datetime
from slistener import SListener
import time, sys
# from python_instagram import get_access_token

client_id='7fa959a59882475ba2231140f893bdf1'
client_secret='a7b40449a691447bb440add4141ac11e'
api = InstagramAPI(client_id = client_id, client_secret = client_secret)

# def access():

#     if len(sys.argv) > 1 and sys.argv[1] == 'local':
#         try:

#             InstagramAPI.host = test_host
#             InstagramAPI.base_path = test_base_path
#             InstagramAPI.access_token_field = "access_token"
#             InstagramAPI.authorize_url = test_authorize_url
#             InstagramAPI.access_token_url = test_access_token_url
#             InstagramAPI.protocol = test_protocol
#         except Exception:
#             pass

#     client_id = raw_input("Client ID: ").strip()
#     client_secret = raw_input("Client Secret: ").strip()
#     redirect_uri = raw_input("Redirect URI: ").strip()
#     raw_scope = raw_input("Requested scope (separated by spaces, blank for just basic read): ").strip()
#     scope = raw_scope.split(' ')
#     # For basic, API seems to need to be set explicitly
#     if not scope or scope == [""]:
#         scope = ["basic"]

#     api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
#     redirect_uri = api.get_authorize_login_url(scope = scope)

#     print "Visit this page and authorize access in your browser:\n", redirect_uri

#     code = raw_input("Paste in code in query string after redirect: ").strip()

#     access_token = api.exchange_code_for_access_token(code)
#     print "access token:\n", access_token

def insta():  
    popular_media = api.media_popular(count=20)
    for media in popular_media:
        print media.images['standard_resolution'].url      
    l = api.location_search(distance = 5000, lat = 41.8954, lng =-87.6243, count = 1000)
    s = Service.objects.get(name="instagram")
    for x in l:
        lat = x["latitude"]
        lon = x["longitude"]  
        find = Post.objects.filter(identifier = x.id, service = s)
        if len(find) == 0:
            post = Post(service = s, latitude = lat, longitude = lon, identifier = x.id, text = x.text, link = "", image = "", timestamp = x.created_at)
            #post.save()
            print("lat: " + lat + " long: " + lon)

    
