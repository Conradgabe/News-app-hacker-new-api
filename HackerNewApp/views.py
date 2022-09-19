from django.shortcuts import render
import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics

from .models import News, Story, Comment, Ask, Job, Poll, Pollopt
from .serializers import ItemSerializer
from .pagination import CustomPageNumberPagination

def make_request(request):

    # while True:
    url = "https://hacker-news.firebaseio.com/v0/beststories.json"

    payload = "{}"
    responses = requests.request("GET", url, data=payload).json()

    for response in responses:
        res = response
        url =  f"https://hacker-news.firebaseio.com/v0/item/{res}.json"

        payload = "{}"
        responses = requests.request("GET", url, data=payload).json()

        db = News.objects.create(
                    author=responses['by'], item_id=responses['id'], text=responses['text'], descendants=responses['descendants'], 
                    time=responses['time'], title=responses['title'], kids=responses['kids'], parent=responses['parent'],
                    type_of=responses['type'], score=responses['score'], parts=responses['parts'],  poll=responses['poll'],
                    url=responses['url'], 
        )
        db.save()
        
        if responses['type'] == story:
            type_story = Story.objects.create(
                    author=responses['by'], item_id=responses['id'], descendants=responses['descendants'],
                    kids=responses['kids'], time=responses['time'], title=responses['title'], type_of=responses['type'],
                    url=responses['url'], score=responses['score'],
            )
            type_story.save()
        
        elif responses['type'] == comment:
            type_comment = Comment.objects.create(
                    author=responses['by'], item_id=responses['id'], text=responses['text'],
                    kids=responses['kids'], parent=responses['parent'], time=responses['time'],
                    type_of=responses['type']
            )
            type_comment.save()
        
        elif responses['type'] == ask:
            type_ask = Ask.objects.create(
                    author=responses['by'], item_id=responses['id'], descendants=responses['descendants'],
                    kids=responses['kids'], time=responses['time'], title=responses['title'], type_of=responses['type'],
                    score=responses['score'], text=responses['text'],
            )
            type_ask.save()

        elif responses['type'] == job:
            type_job = Job.objects.create(
                    author=responses['by'], item_id=responses['id'], text=responses['text'],
                    time=responses['time'], title=responses['title'], url=responses['url'],
                    type_of=responses['type'], score=responses['score'],
            )
            type_job.save()

        elif responses['type'] == poll:
            type_poll = Poll.objects.create(
                    author=responses['by'], item_id=responses['id'], text=responses['text'], descendants=responses['descendants'], 
                    time=responses['time'], title=responses['title'], kids=responses['kids'],
                    type_of=responses['type'], score=responses['score'], parts=responses['parts'],
            )
            type_poll.save()

        elif responses['type'] == pollopt:
            type_pollopt = Pollopt.objects.create(
                    author=responses['by'], item_id=responses['id'], text=responses['text'], poll=responses['poll'],
                    score=responses['score'], time=responses['time'], type_of=responses['type'],
            )
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
    