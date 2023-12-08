from django.db import models
from author.models import Author

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    
    
    def __str__(self) -> str:
        return self.name