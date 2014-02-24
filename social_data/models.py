from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=128)

    def __unicode__(self):
        return "{}, {}".format(self.name, self.icon)

class Post(models.Model):
    service = models.ForeignKey('Service')
    latitude = models.FloatField()
    longitude = models.FloatField()
    identifier = models.CharField(max_length=512)
    text = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return "{} ({},{}) {} {} {} {}".format(self.service.name, self.latitude, self.longitude, self.text, self.link, self.image, self.timestamp)

    


