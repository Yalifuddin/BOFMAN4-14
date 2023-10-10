from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='landing'),
    path('about', views.about_view, name='about'),
    path('gallery', views.gallery_view, name='gallery'),
    path('merch', views.merch_view, name='merch'),
    path('perform', views.perform_view, name='perform'),
]
