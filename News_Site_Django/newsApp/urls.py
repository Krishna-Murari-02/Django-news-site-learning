



from django.urls import path
# from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('latest/',views.latest,name="latest"),
    path('indianarmy/',views.indArmy,name="army"),
    path('indianpara/',views.indPara,name="para"),
    path('indiannavy/',views.indNavy,name="navy"),
    path('content/',views.allContent,name="fullContent"),
    path('newsapi/',views.newsapi,name = 'newsapi'),
    path('breakapi/', views.breakingapi)
    
]