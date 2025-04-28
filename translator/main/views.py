"""from django.shortcuts import render
from django.shortcuts import render,HttpResponse 
from translate import Translator 
# Create your views here. 
  
def home(request): 
    if request.method == "POST": 
        text = request.POST["translate"] 
        language = request.POST["language"] 
        translator= Translator(to_lang=language) 
        translation = translator.translate(text) 
        return HttpResponse(translation) 
    return render(request,"index.html")"""
# Create your views here.
from django.shortcuts import render
from deep_translator import GoogleTranslator
def home(request):
    translated_text = None

    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")

        if text and language:
            translated_text = GoogleTranslator(source="auto", target=language).translate(text)

    return render(request, "home.html", {"translated_text": translated_text})
   

def translate_text(request):
    translated_text = None
    if request.method == "POST":
        input_text = request.POST.get("text")  # Get text from form input
        target_language = request.POST.get("language", "hi")  # Default: Hindi
        
        if input_text:
            translator = GoogleTranslator(source="auto", target=target_language)
            translated_text = translator.translate(input_text)

    return render(request, "translate.html", {"translated_text": translated_text})



