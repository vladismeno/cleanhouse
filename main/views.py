from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm
from .models import Review
from .handlers import AppointmentHandler


class IndexView(View):
    def get(self, request: object) -> object:
        form = AppointmentForm()
        reviews = Review.objects.all().order_by('-date')
        return render(request, 'index.html', {'form': form, 'reviews': reviews})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if AppointmentHandler.process_form_and_send_email(request, form):
            return redirect('index')

        reviews = Review.objects.all().order_by('-date')
        return render(request, 'index.html', {'form': form, 'reviews': reviews})
