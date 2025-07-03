from django.urls import path 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
class custom(LoginView) : 
    template_name = 'tasks/user.html'
    # redirect_authenticated_user = True  
    success_url = reverse_lazy('index') 
from . import views 
from .views import Register 
urlpatterns = [                                                              
    path('',views.index,name="index"),                        
    path('add/',views.add, name="add"),                       
    path('remove/<str:task_id>',views.remove , name="remove") ,  
    path('update/<str:task_id>',views.update , name="update") ,  
    path('login/',custom.as_view(),name="login"),  
    path('logout/',views.logout_view,name="logout") ,  
    path('register/',Register.as_view(),name="register"),    
]                                                                                                                                                                                                                                            