from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('detail/',views.detail,name='detail'),
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('meme/',views.meme,name='meme'),
]