from django.shortcuts import render
import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics

from .models import News
from .serializers import ItemSerializer
from .pagination import CustomPageNumberPagination

def make_request(request):

    while True:
        url = "https://hacker-news.firebaseio.com/v0/beststories.json"

        payload = "{}"
        responses = requests.request("GET", url, data=payload).json()

        for response in responses[0:100]:
            # print(response)
            # return response
            db = News.objects.create(item_id=response)
            db.save()
        # time.sleep(300)

    return render(request, 'index.html', {'res': response})

class ItemList(APIView):

    def get(self, request, format=None):

        queryset = News.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

class ItemFilter(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = News.objects.all()

        item_typeof = self.request.query_params.get('item_typeof')
        if item_typeof:
            queryset = queryset.filter(item_id=item_typeof)

        serializer = ItemSerializer(queryset, many=True)

        return Response(serializer.data)

class ItemSearch(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = ItemSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['^item_id']

class ItemUpdate(APIView):

    def post(self, request, pk, *args, **kwargs):
        queryset = News.objects.get(id=pk)
        serializer = ItemSerializer(instance=queryset, many=True)
        return Response(serializer.data)

class ItemDelete(APIView):

    def get(self, request, pk):
        queryset = News.objects.get(id=pk)
        queryset.delete()
        return Response('Item successfully deleted')
    