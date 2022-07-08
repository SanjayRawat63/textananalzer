from ssl import Purpose
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index.html')

def analyze(request):
    
    djtext=request.GET.get('text','default')
    purpose=""
    remove_puc=request.GET.get('removepunc','off')
    
    capital_text=request.GET.get('capitalize','off')
    
    newline_rem=request.GET.get('newlineremove','off')

    char_count= request.GET.get('charcount','off')

    if remove_puc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        purpose=purpose+"Remove Punctutations "
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
    if capital_text=='on':
        analyzed=""
        purpose =purpose +"Capitalize Text "
        for char in djtext:
            analyzed =analyzed+ char.upper()
        djtext=analyzed
    if newline_rem=='on':
        analyzed=""
        purpose =purpose +"New Line Remover "
        for char in djtext:
            if char !='\n':
                analyzed= analyzed+char
        djtext=analyzed
        params={'purpose':purpose,'analyzed_text':djtext}
        return render(request,'analyze.html',params)        
    else:
        return HttpResponse("Error")