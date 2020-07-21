from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from mainwebsite.models import visitorquery

# Create your views here.

def home(request):
    template_name = "mainwebsite/index.html"
    return render(request,template_name,{"homepage":"active"})


def contactus(request):
    template_name = "mainwebsite/contactus.html"
    return render(request,template_name,{"contactus":"active"})

def services(request):
    template_name = "mainwebsite/blog.html"
    return render(request,template_name,{"contactus":"active"})

def sendquery(request):
    if request.method == 'POST':
        subject = "A new Message from your website"
        message_body = "First Name: " + str(request.POST['first_name']) + "\nLast Name: " + str(request.POST['last_name']) + "\nEmail ID: " + str(request.POST['email']) + "\nContact Number: " + str(request.POST['contactnumber']) + "\n ------------------Message here------------------------\n Message : " + str(request.POST['message'])
    
        visitor = visitorquery(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'], contactnumber = request.POST['contactnumber'], message = request.POST['message'])
    
        visitor.save()
        try:
            send_mail(subject,message_body,'narendra@slicservices.in',['narendra@slickservices.in'],fail_silently=False)
        except:
            print("Email not sent")
    
    return redirect("/")
