from django.conf.urls import patterns, url
from users import views
urlpatterns = patterns('',
url(r'^$', views.register, name='register'),
url(r'^signin', views.signIn, name='signin')
)
