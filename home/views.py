from django.shortcuts import render, redirect
from .models import Chambre, Catalogue, Testimonial, ReservationForm
# from django.http import HttpResponse

# Create your views here.


def index(request):
    chambres = Chambre.objects.all()
    catalogues = Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "chambres": chambres,
        "catalogues": catalogues,
        "testimonials": testimonials,
    }
    return render(request, "index.html", context)


# Ensure this import is correct based on your project structure


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            reservation = form.save()
            print(f"Reserva guardada: {reservation}")
            return redirect("reservation_confirmation")
        else:
            print("Formulario inválido")
            print(form.errors)
    else:
        form = ReservationForm()
    return render(request, "reservation.html", {"form": form})


def reservation_confirmation(request):
    return render(request, "reservation_confirmation.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    chambres = Chambre.objects.all()
    return render(request, "blog.html", {"chambres": chambres})


def about(request):
    return render(request, "about.html")
