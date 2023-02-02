from django.db import models as m
from test1.models import Post

# Create your models here.


class Comment(m.Model):
    rise = m.CharField(max_length=50)
    post = m.ForeignKey(Post, on_delete=m.CASCADE)

    def __str__(self) -> str:
        return self.rise

