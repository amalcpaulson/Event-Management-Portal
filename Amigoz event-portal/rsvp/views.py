
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def send_book(email,event,name):
    subject = f"Booking successfull for {event}"
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    contact_msg = f"Dear,{name},\n\nWe are pleased to inform you that your booking for your Event is Confirmed.\n\n Event Details:\n Event name:{event}\n\nWe are Glad that you're with us and look forward to active participation in the Events.\n\n\n In the meantime you've any queries, Feel Free to contact us via email eventportalbfh@gmail.com, and we'll be happy to help."
    send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)
    return 0
    #return HttpResponse("on send email page")


def send_reg(email, pname):
    subject = f" And you're in the race! - CHRIST Event Registration Successful!"
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    contact_msg = f"Dear {pname},\n\nYour new CHRIST Event Registration Account has been created.\nWelcome to the CHRIST Event community!\n\nFrom now on, please log in to your account using your email address and your password.\n\nIf you received this email but didn't register for an CHRIST Event Account something's gone haywire. \n\nManage Your New Account and Do register for the events you're gonna rock.\n\n\nRegards,\nCHRIST EVENT MANAGEMENT TEAM."
    send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)
    return 0
    #return HttpResponse("on send email page")

