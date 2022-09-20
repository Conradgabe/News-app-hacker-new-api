from django.shortcuts import render
import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.contrib import messages

from .models import News, Story, Comment, Ask, Job, Poll, Pollopt
from .serializers import ItemSerializer, CommentSerializer, AskSerializer, JobSerializer, PollSerializer, PolloptSerializer
from .pagination import CustomPageNumberPagination

def make_request(request):

    while True:
        url = "https://hacker-news.firebaseio.com/v0/beststories.json"

        payload = "{}"
        responses = requests.request("GET", url, data=payload).json()

        for response in responses[0:1]:
            res = response
            url =  f"https://hacker-news.firebaseio.com/v0/item/{res}.json"

            payload = "{}"
            responses = requests.request("GET", url, data=payload).json()

            # db = News.objects.create(
            #             author=str(responses['by']), item_id=str(responses['id']), text=str(responses['text']), descendants=str(responses['descendants']), 
            #             time=str(responses['time']), title=str(responses['title']), kids=str(responses['kids']), parent=str(responses['parent']),
            #             type_of=str(responses['type']), score=str(responses['score']), parts=str(responses['parts']),  poll=str(responses['poll']),
            #             url=str(responses['url']), 
            # )
            # db.save()
            print(responses)
            if responses['type'] == 'story':
                type_story = Story.objects.create(
                        author=responses['by'], item_id=responses['id'], descendants=responses['descendants'],
                        kids=responses['kids'], time=responses['time'], title=responses['title'], type_of=responses['type'],
                        score=responses['score'],url=responses['url'],
                )
                # if responses['url'] in responses:
                #     type_story = Story.objects.create(
                #         author=responses['by'], item_id=responses['id'], descendants=responses['descendants'],
                #         kids=responses['kids'], time=responses['time'], title=responses['title'], type_of=responses['type'],
                #         url=responses['url'], score=responses['score'],
                # )
                # else:
                #     continue
                type_story.save()
            
            elif responses['type'] == 'comment':
                type_comment = Comment.objects.create(
                        author=responses['by'], item_id=responses['id'], text=responses['text'],
                        kids=responses['kids'], parent=responses['parent'], time=responses['time'],
                        type_of=responses['type']
                )
                type_comment.save()
            
            elif responses['type'] == 'ask':
                type_ask = Ask.objects.create(
                        author=responses['by'], item_id=responses['id'], descendants=responses['descendants'],
                        kids=responses['kids'], time=responses['time'], title=responses['title'], type_of=responses['type'],
                        score=responses['score'], text=responses['text'],
                )
                type_ask.save()

            elif responses['type'] == 'job':
                type_job = Job.objects.create(
                        author=responses['by'], item_id=responses['id'], text=responses['text'],
                        time=responses['time'], title=responses['title'], url=responses['url'],
                        type_of=responses['type'], score=responses['score'],
                )
                type_job.save()

            elif responses['type'] == 'poll':
                type_poll = Poll.objects.create(
                        author=responses['by'], item_id=responses['id'], text=responses['text'], descendants=responses['descendants'], 
                        time=responses['time'], title=responses['title'], kids=responses['kids'],
                        type_of=responses['type'], score=responses['score'], parts=responses['parts'],
                )
                type_poll.save()

            elif responses['type'] == 'pollopt':
                type_pollopt = Pollopt.objects.create(
                        author=responses['by'], item_id=responses['id'], text=responses['text'], poll=responses['poll'],
                        score=responses['score'], time=responses['time'], type_of=responses['type'],
                )
            # time.sleep(300)

        return render(request, 'index.html', {'res': response})
        time.sleep(300)

class ItemList(APIView):

    def get(self, request, format=None):

        queryset = Story.objects.all()
        queryset_2 = Comment.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        serializer_comment = ItemSerializer(queryset_2, many=True)
        return Response(data=[
            serializer_comment.data, serializer.data
        ])
        

    # def get(self, request, format=None):

        # queryset = Comment.objects.all()
        # serializer_comment = CommentSerializer(queryset, many=True)
        # return Response(serializer_comment.data)

class ItemFilter(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = ItemSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['type_of', 'author']
    

class ItemSearch(generics.ListAPIView):
    # queryset = Story.objects.all()
    # serializer_class = ItemSerializer
    # pagination_class = CustomPageNumberPagination
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # search_fields = ('author')
    pass

class ItemUpdate(APIView):

    def post(self, request, pk, *args, **kwargs):
        queryset = Story.objects.get(id=pk)
        serializer = ItemSerializer(instance=queryset, many=True)
        return Response(serializer.data)

class ItemDelete(APIView):

    def get(self, request, pk):
        queryset = Story.objects.get(id=pk)
        queryset.delete()
        return Response('Item successfully deleted')
    