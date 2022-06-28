from django.db import models
from users.models import User
# Create your models here.

class Summary(models.Model) :
    
    summary = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return self.summary
    class Meta:
        ordering = ('timestamp',) 
