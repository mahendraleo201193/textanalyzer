from django.urls import path
from django.views.generic import TemplateView,ListView
from textAnalyzer.views import *
urlpatterns = [
    path('hello/',hello,name="hello"),
    path('home/',TemplateView.as_view(template_name="home.html"),name="home"),
    path('AnalyzeText/',AnalyzeText,name="AnalyzeText"),
    path('result/',AnalyzeText,name="result")



]