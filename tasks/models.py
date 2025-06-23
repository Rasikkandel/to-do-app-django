from django.db import models
class taskss(models.Model) : 
    taskharu = models.CharField(max_length=40) 
    priority = models.IntegerField()

    def __str__(self) : 
        return self.taskharu 
    
