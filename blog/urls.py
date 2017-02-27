from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    # ?P<id> - django will take a value you pass in the url and transfer it to a view as a variable called id
    # \d+ - id a digit (range 0-9), + means the digit is allowed to occur one or more times.
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/top$', views.top_five),
]