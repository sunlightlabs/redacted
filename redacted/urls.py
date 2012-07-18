from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from redacted.models import Post

admin.autodiscover()


class RedactedView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'


class PostView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):

        resp = super(PostView, self).get(request, *args, **kwargs)

        if request.is_ajax():
            return resp
        else:
            post = resp.context_data['post']
            return HttpResponseRedirect(post.url)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
    url(r'^$', RedactedView.as_view(), name='post_list'),
    url(r'', include('sfapp.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
