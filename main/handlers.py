from django.core.mail import send_mail
from django.contrib import messages


class AppointmentHandler:
    @staticmethod
    def process_form_and_send_email(request, form):
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
            return True  # Успешно обработано
        return False  # Форма недействительна
