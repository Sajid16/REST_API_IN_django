from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Blog.models import Category, Articles
from Blog.serializers import categorySerializer, articlesSerializer

# imports for @api_view based API

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

count = 0


# API with self made functions

# @csrf_exempt
# def blogPosts(request):
#     if request.method == 'GET':
#         article = Articles.objects.all()
#         serializer = articlesSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = articlesSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse('data has been saved successfully to Article', status=201, safe=False)
#         return JsonResponse(serializer.errors, status=400, safe=False)
#
#
# @csrf_exempt
# def blogPostDetails(request, pk):
#     """
#     Retrieve, update or delete a code article.
#     """
#     try:
#         article = Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = articlesSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = articlesSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)


# API with @api_view functions

@api_view(['GET', 'POST'])
def blogPosts(request):
    test = 0
    if request.method == 'GET':
        article = Articles.objects.all()
        serializer = articlesSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        for i in range(len(request.data)):
            print(request.data[i])
            print('test')
            serializer = articlesSerializer(data=request.data[i])
            if serializer.is_valid():
                serializer.save()
                test += 1
        if test == len(request.data):
            return Response('data has been saved successfully to Article', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blogPostDetails(request, pk):
    """
    Retrieve, update or delete a code article.
    """
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = articlesSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = articlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
