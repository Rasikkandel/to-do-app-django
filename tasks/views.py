from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from tasks.models import taskss

def index(request) :                         
    if request.method == "POST":       
        task = request.POST.get('task')     
        prior = request.POST.get('prio')      
        if task: 
            taskss.objects.create(taskharu=task, priority=prior or 1)
        return redirect('kaam:index')            
# redirect instead of render garda refresh garda kheri pheri post hunxa 
    tasks = taskss.objects.all()             
    return render(request, "tasks/index.html", {
        'task': tasks,            
    })                                                                               
def add(request) :                     
    return render(request,"tasks/add.html")             

def remove(request, task_id): 
    task = get_object_or_404(taskss, pk=task_id)
    task.delete()                       
    return redirect('kaam:index')  


def update(request , task_id) : 
    if(request.method=="POST") : 
        task = taskss.objects.get(pk=task_id)                      
        task.taskharu = request.POST.get("task")            
        task.priority = request.POST.get("prio")   
        task.save()                                           
        return redirect('kaam:index')                                
    task = taskss.objects.get(pk=task_id) 
    return render(request ,"tasks/update.html", {'task':task})        
