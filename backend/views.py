# for function based views
from django.shortcuts import render
from .models import Article 
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# For api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# for class based views
from rest_framework.views import APIView

# working with mixins 
from rest_framework import mixins
from rest_framework import generics

# for viewsets
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'    



""" 
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    queryset  = Article.objects.all()
    serializer_class = ArticleSerializer
"""


""" 
class ArticleViewSet(viewsets.ViewSet):
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
"""

""" 
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='slug'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
"""
