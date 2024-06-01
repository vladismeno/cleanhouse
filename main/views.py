from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm
from .models import Review
from .handlers import AppointmentHandler
from django.conf import settings


class IndexView(View):
    def get(self, request: object) -> object:
        form = AppointmentForm()
        reviews = Review.objects.all().order_by('-date')
        context = {
            'form': form,
            'reviews': reviews,
            'email': settings.EMAIL,
            'phone': settings.PHONE,
            'address': settings.ADDRESS,
            'facebook': settings.FACEBOOK,
            'instagram': settings.INSTAGRAM,
            'years_experienced': settings.YEARS_EXPERIENCED,
            'happy_customers': settings.HAPPY_CUSTOMERS,
            'building_cleaned': settings.BUILDING_CLEANED,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = AppointmentForm(request.POST)
        if AppointmentHandler.process_form_and_send_email(request, form):
            return redirect('index')

        return render(request, 'index.html', {'form': form})
