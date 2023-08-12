from django.urls import path

from .views import blog_view, home_view, robots_view, sitemap_view

urlpatterns = [
    path("", home_view, name="home"),
    path("blog", blog_view, name="blog"),
    path("sitemap.xml", sitemap_view, name="sitemap"),
    path("robots.txt", robots_view, name="robots"),
]
