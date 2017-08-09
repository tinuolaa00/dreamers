from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.post_list, name= 'post_list'),
    url(r'^page/(?P<page_name>[\w\-\&]+)', views.static_page, name='page'),
]
