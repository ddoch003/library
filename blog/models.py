from django.db import models
from django.contrib.auth import get_user_model

# An abstract mixin class could have been added but the migrations were already applied so the BlogPostComment was written standalone

UserModel = get_user_model()


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class BlogPostComment(models.Model):
    to_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
