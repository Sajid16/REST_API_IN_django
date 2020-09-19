from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        print('here')
        file_serializer = FileSerializer(data=request.data)
        print('here1')

        if file_serializer.is_valid():
            print('here2')
            file_serializer.save()
            print('here3')
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('here4')
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
