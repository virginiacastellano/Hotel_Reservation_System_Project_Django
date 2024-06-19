from django.shortcuts import render
from home.models import Chambre
# Create your views here.
def allRooms (request):
   chambres = Chambre.objects.all()
   return render(request, 'rooms.html', {'Chambres': chambres})

