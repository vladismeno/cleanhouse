from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import AppointmentForm
from .models import Review


def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            services = form.cleaned_data['services']
            cleaner = form.cleaned_data['cleaner']
            # Handle the form data (e.g., save to database, send email, etc.)

            # Send an email
            subject = 'New Appointment Request'
            message = f'Name: {name}\nPhone Number: {phone_number}\nObject: {services}\nCleaner: {cleaner}'
            from_email = 'vladismeno@gmail.com'
            recipient_list = ['vladismeno@gmail.com']  # Replace with recipient's email

            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Форма успешно отправлена!')

            return redirect('index')
    else:
        form = AppointmentForm()

    reviews = Review.objects.all().order_by('-date')
    return render(request, 'index.html', {'form': form, 'reviews': reviews})