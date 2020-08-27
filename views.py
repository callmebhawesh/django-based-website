from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1':"this is variable one",
        'variable2':"This is variable two"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about us page")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST .get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thanks for reaching us.')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact us page")
def privacy(request):
    return render(request, 'privacy.html')
    # return HttpResponse("this is privacy page")