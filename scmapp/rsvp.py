import smtplib, ssl
from scmapp.models import User, Admin, Event, Book_ground, Admission
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
for e in User.email:

    receiver_email = e.User.email
    password = input("Type your password and press enter:")
    message = """\
Subject: Hi there

This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)