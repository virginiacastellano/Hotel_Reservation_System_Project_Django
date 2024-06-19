from django.urls import path
from .views import index, reservation, contact, blog, about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('reservation/', reservation, name='reservation'),
    path('reservation/confirmation/', views.reservation_confirmation, name='reservation_confirmation'),    path('Contact/', contact, name='Contact'),
    path('Blog/', blog, name='Blog'),
    path('About/', about, name='About'),
]

urlpatterns += staticfiles_urlpatterns()
