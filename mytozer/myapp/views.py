from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,render,get_object_or_404
from myapp.talk import talkk
import wikipedia

# Create your views here.
def myhome(request):
    talkk("welcome to tozer app, insert data so i can read sir.")
    return render(request,'home.html')

def read(request):
    mytext=request.POST['mytext']
    result=wikipedia.summary(mytext)
    result1=wikipedia.summary(mytext,sentences=2)
    pic=wikipedia.page(mytext).images
    one_pic=pic[0]
    talkk(result1+"," +" here is some more imformation about "+ mytext)
    return render(request,'home.html',{'pics':one_pic,'sum':result,'title':mytext})
    
    
    
    


    
