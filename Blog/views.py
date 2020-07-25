from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Blog.models import Category, Articles
from Blog.serializers import categorySerializer, articlesSerializer

# Create your views here.


@csrf_exempt
def blogPosts(request):
    if request.method == 'GET':
        article = Articles.objects.all()
        serializer = articlesSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = articlesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('data has been saved successfully to Article', status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


@csrf_exempt
def blogPostDetails(request, pk):
    """
    Retrieve, update or delete a code article.
    """
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = articlesSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = articlesSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
