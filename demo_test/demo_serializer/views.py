from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment

class CommentView(APIView):

    def get(self,request):
        queryset=Comment.objects.all() #list of objects
        serializer=CommentSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  
    # def __init__(self,email,content,created=None):
    #     self.email=email
    #     self.content=content
    #     self.created=created or datetime.now()

    # def get(self,request,*args,**kwargs):
    #     serializer=CommentSerializer(comment)
    #     return Response(serializer.data)


# comment=Comment(email="babisantos34@gmail.com",content="Work Hard, Play Hard")
# serializer=CommentSerializer(comment)