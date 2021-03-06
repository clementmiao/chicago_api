# Chicago Location Mapping
## by Clement Miao, Sam Przezdziecki, and Charlie Fisher

link to website: http://obscure-caverns-2114.herokuapp.com/
project can be found on github at: https://github.com/clementmiao/chicago_api

Chicago Location Mapping takes data from Twitter, Instagram, and Facebook and overlays this data on a google map.


Setup process:

1. install necessary packages
 `pip install -r requirements.txt`

2. sync database
 `python manage.py syncdb`

3. to start the server
 `foreman start` 
  
Descriptions:
For the google map base, the code is in the gmap folder. The templatetags folder contains the basic maps that we use, and the templates folder contains the javascript code for displaying the markers and posts themselves in map.html, and the javascript for the sentiment analysis in map_sentiment.html

The data management files are in the social_data folder. Our website currently has posts centered around Chicago (41.8954, -87.6243), but to get data around any latitude and longitude coordinates, do the following:

For Twitter:
    From the command line, navigate to the chicago_api folder and run: python manage.py shell
    Once in the shell type: `from social_data.twitter import twitter`
    Then type: `twitter(lat, lon, radius)` where lat and lon are the latitude and longitude of the desired point, and radius is the desired radius in kilometers
 
 For Instagram:
    From the command line, navigate to the chicago_api folder and run: python manage.py shell
    Once in the shell type: `from social_data.insta import instagram`
    Then type: `instagram(lat, lon, radius)` where lat and lon are the latitude and longitude of the desired point, and radius is the desired radius in kilometers
    
For Facebook:
    From the command line, navigate to the chicago_api folder and run: python manage.py shell
    Once in the shell type: `from social_data.facebook import facebook`
    Then type: `facebook(lat, lon, radius)` where lat and lon are the latitude and longitude of the desired point, and radius is the desired radius in kilometers
    
The APIs represent latitude and longitude coordinates as floats from -180.0 to 180. North of the equator is positive, south of the equator is negative, east of the prime meridian is positive, and west is negative.


Twitter Sentiment Analysis labels twitter posts as positive or negative using the NLTK python library. The files to train a model can be found in social_data/twitter_data. Our sentiment analysis baysian classifier can be found in the my_classifier.pickle file.


The City of Chicago provides a kml file with the geographical coordinate boundaries of the neighborhoods of Chicago. Our code counts the number of tweets from each neighborhood and the number of positive tweets, and calculates the percent of tweets that are positive. Based on the result, we shade the neighborhood a different color.

In social_data/nlp.py run `process_tweets()` to populate the sentiment table

