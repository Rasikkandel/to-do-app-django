from django.shortcuts import render
import datetime 
# Create your views here.
def index(request) : 
    now = datetime.datetime.now() 
    if(now.month == 6 and now.day== 19) : 
        ny = True 
    else : 
        ny = False 
    return render(request,"newyear/index.html",
    { 
        'ny' : ny 
    })    
    
