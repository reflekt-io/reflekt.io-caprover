import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from about_us.models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST' and  request.is_ajax():
        form = ContactForm(request.POST)
        data = {}

        if form.is_valid():
            form.save()
            data['success'] = True
            return JsonResponse(data)
        else:
            data['success'] = False
            return JsonResponse(data)
        
    else:
        form = ContactForm()
        return render(request, 'about_us_index.html', {'form':form})

@csrf_exempt
def add_contact_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
    
        full_name = data["full_name"]
        query_topic = data["query_topic"]
        phone_number = data["phone_number"]
        email = data["email"]
        message = data["message"]

        contact = Contact(full_name=full_name, query_topic=query_topic, phone_number=phone_number, email=email, message=message)

        contact.save()

        return JsonResponse({"status": "success"}, status=200)
       
    else:
        return JsonResponse({"status": "error"}, status=401)
