from django.shortcuts import render
from .models import new,Breaking
from rest_framework.response import Response
from .serializers import newSerializers,BreakingSerializers
from rest_framework.decorators import api_view

# from News_Site_Django.newsApp import serializers
# from import serializers
# Create your views here.

def home(request):
    # big = new.objects.all()
    breaking = Breaking.objects.all()
    len1 = len(breaking)
    breaking = breaking[len1-1].breaking
    # print(breaking[len1-1].breaking)
    top_stories = new.objects.filter(news_category ='Top Stories').order_by('-id')[:4]
    militry = new.objects.filter(news_category ='Militry' ).order_by('-id')[:4]
    paramilitry = new.objects.filter(news_category ='Paramilitry' ).order_by('-id')[:4]
    navy = new.objects.filter(news_category ='Navy' )[:4]
    latest = new.objects.all().order_by('-id')[:3]

    return render(request,'newsApp/home.html', {'breaking':breaking,'top_stories': top_stories, 
    'militry':militry, 'paramilitry':paramilitry, 
    'navy':navy, 'latest':latest})


def allContent(request):
    pass

def latest(request):
   
    latest_page = new.objects.all().order_by('-id')
    return render(request,'newsApp/latest.html', {'latest': latest_page })

def indArmy(request):
    army = new.objects.filter(news_category ='Militry')
    return render(request,'newsApp/latest.html', {'indarmnew': army })

def indPara(request):
    para = new.objects.filter(news_category ='paramilitry')
    return render(request,'newsApp/latest.html', {'indparanew': para })

def indNavy(request):
    navy = new.objects.filter(news_category ='Navy')
    return render(request,'newsApp/latest.html', {'indnavynew': navy })


    
@api_view(['GET'])
def newsapi(request):
    if request.method == 'GET': 
        news= new.objects.all()
        serializer = newSerializers(news,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def breakingapi(request):
    if request.method == 'GET':
      
        
        breaki = Breaking.objects.all()
        serializer = BreakingSerializers(breaki,many=True)
        return Response(serializer.data)


    






