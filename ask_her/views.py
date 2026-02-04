from django.shortcuts import render
from django.http import JsonResponse
from .models import Response

# Create your views here.
def home(request):
    if request.method == "POST":
        # Save the "Yes" to the database
        Response.objects.create(answer="YES")
        return JsonResponse({"status": "success"})
    
    return render(request, 'index.html')