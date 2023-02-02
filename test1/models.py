from django.db import models as m

# Create your models here.

class Post(m.Model):
    title = m.CharField(max_length=50)
    discription = m.TextField()

    def __str__(self) -> str:
        return self.title
    

