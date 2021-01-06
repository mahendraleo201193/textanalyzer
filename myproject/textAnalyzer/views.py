from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from textAnalyzer.forms import TextAnalyzerForm

def hello(request):
   text = """<h1>welcome to my textAnalyzer !</h1>"""
   return HttpResponse(text)

def AnalyzeText(request):
   result = {}
   
   if request.method == "POST":
      #Get the posted form
      MyTextAnalyzerForm = TextAnalyzerForm(request.POST, request.FILES)
      
      if MyTextAnalyzerForm.is_valid():
         
         name = MyTextAnalyzerForm.cleaned_data["name"]
         file = MyTextAnalyzerForm.cleaned_data["file"]
         data = file.read().decode("utf-8") 
         print("##########")
         print(data.strip())
         result = freq(data)
         #profile.save()
         #saved = True
		
   return render(request, 'result.html', locals())

def freq(str): 
  
    # break the string into list of words 
    str_list = str.lower().split() 
    result = {}
    # gives set of unique words 
    unique_words = set(str_list) 
      
    for words in unique_words :
        result[words]= str_list.count(words)
        #print('Frequency of ', words , 'is :', str_list.count(words)) 
    return result
  