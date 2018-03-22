# Built in import
from django.conf.urls import url, include
from django.views.generic import TemplateView

# app import
from .views import home
from .api import views as api_view

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^api/users/$', api_view.UserListCreateView.as_view(), name='list-create'),
    url(r'^api/users/(?P<id>\d+)/$', api_view.UserRetrieveUpdateDestroyView.as_view(), name='rud')
]