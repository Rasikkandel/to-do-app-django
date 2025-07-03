from django.db import models
from django.contrib.auth.models import User 
class taskss(models.Model) : 
    User = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True) 
    taskharu = models.CharField(max_length=40) 
    priority = models.IntegerField()
    completion = models.BooleanField(default=False) 

    class meta : 
        ordering = ["completion"]

    # def __str__(self) : 
    #     return self.taskharu 
    
