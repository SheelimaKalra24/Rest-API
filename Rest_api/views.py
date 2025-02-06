from django.shortcuts import render
from rest_framework .views import APIView
from .models import post
from .Serializers import postSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class api_views(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                query = post.objects.get(pk=pk)
            except:
                return Response({'error': "data is not found"},status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = postSerializer(query)
                return Response(serializer.data , status=status.HTTP_200_OK)
        query_set = post.objects.all()
        serializer = postSerializer(query_set,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = postSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response({'error': "request is not accepted"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            post_instance = post.objects.get(pk=pk)
        except:
            return Response({'error': "data is not found"},status=status.HTTP_400_BAD_REQUEST)
        serializer = postSerializer(post_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response({'error': "request is not accepted"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            post_instance = post.objects.get(pk=pk)
        except:
            return Response({'error': "data is not found"},status=status.HTTP_400_BAD_REQUEST)
        post_instance.delete()
        return Response({'message': "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
