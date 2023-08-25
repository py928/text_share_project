from django.db import models

# Create your models here.
from django.db import models

class TXT(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=20)