from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

# def icon(request, service_id):
#     try:
#         icon = Service.objects.get(id=service_id)

#     c = {
#         'icon': icon,        
#     }

#     return render(request, 'social_data/icon.html', c) 