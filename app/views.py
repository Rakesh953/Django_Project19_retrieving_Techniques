from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

from django.db.models.functions import Length
# Create your views here.

def insert_topic(request):
    tn=input('Enter topic:-')

    TTO=Topic.objects.get_or_create(topic_name=tn)
    bl=TTO[1]
    
    if bl:
        TO=TTO[0]
        TO.save()
        d={'topics':Topic.objects.all()}
        # return HttpResponse('Topic is created')
        return render(request,'retrieve_topic.html',d)
    else:
        return HttpResponse('Topic is already present')



'''
#getting PO by using get method so if object is not there then Throws an error
def insert_webpage(request):
    tn=input('enter topicname')

    TO=Topic.objects.get(topic_name=tn)
    na=input('enter name')
    url=input('enter url')
    email=input('enter email')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
    WO.save()
    return HttpResponse('webpage is created')
'''

def insert_webpage(request):
    tn=input('Enter topic_name:')
    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        na=input('enter name')
        url=input('enter url')
        email=input('enter email')

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('Topic is not there so i cant create ur webepage object')



def retrieve_topic(request):
    d={'topics':Topic.objects.all()}
    return render(request,'retrieve_topic.html',d)

# # it will get all the object of webpage:-
# def webepage_retrieve(request):   
#     d={'webpage':Webpage.objects.all()}
#     return render(request,'webepage_retrieve.html',d)


# It will get the specific object of the given condition in filter:-
def webepage_retrieve(request):
    QLWO=Webpage.objects.all()[::-2]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(topic_name='Cricket')
    d={'webpage':QLWO}
    return render(request,'webepage_retrieve.html',d)