from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import uuid


def send_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    sender_email = 'rk8449022182@gmail.com' # Replace with your email address
    recipient_list = ['rahulhaibatpur022@gmail.com']  # List of recipient email addresses
    send_mail(subject, message, sender_email, recipient_list)
    return HttpResponse('Email sent successfully')


def home(request):
    token=uuid.uuid4()
    print(token)
    return HttpResponse("your email send")