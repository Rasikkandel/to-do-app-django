from django.urls import path 
from . import views 
app_name = "kaam"
urlpatterns = [                                                             
    path('',views.index,name="index"),
    path('/add',views.add , name="add"),            
    path('remove/<str:task_id>',views.remove , name="remove") ,  
    path('update/<str:task_id>',views.update , name="update") ,           
]                                                                                                                                                                                                                                        