from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm
from .models import Review
from .handlers import AppointmentHandler
from django.conf import settings
from django_user_agents.utils import get_user_agent


def error_404_view(request, exception):
    return render(request, '404.html', status=404)


class IndexView(View):

    def is_mobile(self, request):
        user_agent = get_user_agent(request)
        return user_agent.is_mobile

    def get(self, request: object) -> object:
        form = AppointmentForm()
        reviews = Review.objects.all().order_by('-date')
        is_mobile = self.is_mobile(request)
        facebook = settings.FACEBOOK_MOBILE if is_mobile else settings.FACEBOOK_DESKTOP
        instagram = settings.INSTAGRAM_MOBILE if is_mobile else settings.INSTAGRAM_DESKTOP

        context = {
            'form': form,
            'reviews': reviews,
            'email': settings.EMAIL,
            'phone': settings.PHONE,
            'address': settings.ADDRESS,
            'facebook': facebook,
            'instagram': instagram,
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
