from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.models import taskss 
from django.contrib.auth import logout , login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# FIXED: Added login_required decorator and fixed field name
@login_required
def index(request):                         
    if request.method == "POST":       
        task = request.POST.get('task')     
        prior = request.POST.get('prio')      
        if task: 
            # FIXED: Use 'User' (capital U) to match your model field
            taskss.objects.create(
                taskharu=task, 
                priority=prior or 1,
                User=request.user  # Use 'User' to match your model field
            )                                                                                
        return redirect('index')                        
    
    # FIXED: Use 'User' (capital U) to match your model field name
    tasks = taskss.objects.filter(User=request.user)  
    search_input = request.GET.get('search-name') or ''
    if search_input : 
        tasks = tasks.filter(taskharu__icontains=search_input)

    return render(request, "tasks/index.html", {
        'task': tasks,  
        'search_input' : search_input ,       
    })                                             

@login_required                                                                                       
def add(request):                     
    return render(request, "tasks/add.html")                 

# FIXED: Added user permission check
@login_required
def remove(request, task_id): 
    # FIXED: Use 'User' (capital U) to match your model field
    task = get_object_or_404(taskss, pk=task_id, User=request.user)
    task.delete()                                   
    return redirect('index')  

# FIXED: Added user permission check and error handling
@login_required
def update(request, task_id): 
    # FIXED: Use 'User' (capital U) to match your model field
    task = get_object_or_404(taskss, pk=task_id, User=request.user)
    
    if request.method == "POST": 
        task.taskharu = request.POST.get("task")            
        task.priority = request.POST.get("prio") or 1  # FIXED: Added default value
        task.save()                                           
        return redirect('index')                                
    
    return render(request, "tasks/update.html", {'task': task})        

def logout_view(request):
    logout(request) 
    messages.success(request, "You have been logged out successfully")
    return redirect('index')

class Register(FormView) : 
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index') 

    def form_valid(self , form) : 
        user = form.save() 
        if user is not None : 
            login(self.request , user) 
        return super(Register , self).form_valid(form)

