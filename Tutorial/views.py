from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def test(request):
    # message = {"it is working properly"}
    return JsonResponse({"it is working properly"})
    # return HttpResponse("it is working properly")
