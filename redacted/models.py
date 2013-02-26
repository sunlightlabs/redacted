import datetime

from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    scribd_embed = models.TextField(blank=True)
    date_posted = models.DateField(default=datetime.date.today)
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails')

    class Meta:
        ordering = ('-date_posted',)

    def __unicode__(self):
        return self.title
