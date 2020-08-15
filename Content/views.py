from django.shortcuts import render

# Create your views here.

def contentList(request):
    return render(request, 'apiList.html')
