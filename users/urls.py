from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework import routers

from .api import views as api_view

router = routers.DefaultRouter()
router.register(r'api/users', api_view.UserViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^', include(router.urls)),
]