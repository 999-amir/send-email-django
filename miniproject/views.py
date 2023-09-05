from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.mail import send_mail


class EmailTestView(View):
    def get(self, request):
        title = 'title of email'
        message = 'message of email'
        send_to = ['user_email@gmail.com']  # all users email

        send_mail(title, message, 'settings.EMAIL_HOST_USER', send_to, fail_silently=False)
        return HttpResponse('email send successfully')
