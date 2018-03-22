from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework import routers

from .api import views as api_view

# router = routers.DefaultRouter()
# router.register(r'api/users', api_view.UserViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^api/users/$', api_view.UserListCreateView.as_view(), name='list-create'),
    url(r'^api/users/(?P<id>\d+)/$', api_view.UserRetrieveUpdateDestroyView.as_view(), name='rud')
]