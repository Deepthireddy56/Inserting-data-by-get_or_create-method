from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Insert_topic(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('TOPIC DATA IS INSERTED')
def Insert_Webpage(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('WEBPAGE DATA IS INSERTED')
def Insert_Access_Records(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('Enter Date: ')
    a=input('Enter Author_name: ')
    ao=Access_Records.objects.get_or_create(name=wo,date=d,author=a)
    return HttpResponse('ACCESS RECORDS DATA IS INSERTED')