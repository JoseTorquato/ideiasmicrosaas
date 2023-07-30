from django.urls import path

from .views import home_view,sitemap_view

urlpatterns = [
    path("", home_view, name="home"),
    path("sitemap.xml", sitemap_view, name="sitemap"),
]
