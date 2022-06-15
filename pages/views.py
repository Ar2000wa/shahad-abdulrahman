from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
   return render(request,'pages/home.html')
def about(request):
   return render(request, 'pages/about.html')


def contact(request):
   if request.method == 'POST':
      # GET DATA FROM (FORM)
      v_name = request.POST.get('name')
      v_email = request.POST.get('email')
      v_massage = request.POST.get('message')
      # SEND DATA TO DATABASE
      v_contact = Contact(name=v_name, email=v_email, massage=v_massage)
      v_contact.save()
      return render(request, 'pages/thanks.html')
   else:
      return render(request,'pages/contact.html')
