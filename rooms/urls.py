from django.urls import path
from .views import allRooms
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('allRooms/', allRooms, name='allRooms'),
]

urlpatterns += staticfiles_urlpatterns()
