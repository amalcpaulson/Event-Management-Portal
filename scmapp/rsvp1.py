import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
from scmapp.models import User, Admin, Event, Book_ground, Admission
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

def rsvp(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    time = request.POST.get('time')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')

    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            print(f"Sending email to {name}")
            # Send email here

    sender_email = "admin@gmail.com"
    receiver_email = "your@gmail.com"
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

# Create the plain-text and HTML version of your message
    text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

