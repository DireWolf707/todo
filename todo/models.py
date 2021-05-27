from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=60)
    memo = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})
    
    
    