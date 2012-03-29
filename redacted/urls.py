from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

from redacted.models import Post

admin.autodiscover()

class RedactedView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'

urlpatterns = patterns('',
    url(r'^$', RedactedView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )