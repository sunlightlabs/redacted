import datetime

from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(help_text="This field is not displayed to users", blank=True)
    date_posted = models.DateField(default=datetime.date.today)
    url = models.URLField(verify_exists=False)
    thumbnail = models.ImageField(upload_to='redacted')

    class Meta:
        ordering = ('-date_posted',)

    def __unicode__(self):
        return self.title
