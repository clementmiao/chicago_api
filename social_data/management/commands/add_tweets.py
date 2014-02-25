# you MUST import the management classes like this:
from django.core.management.base import NoArgsCommand, CommandError
from social_data.twitter import twitter

class Command(NoArgsCommand):
    help = "Adds tweets to the database"

    def handle_noargs(self, **options):
        # print "Hello World"
        for i in range(8):
            twitter()