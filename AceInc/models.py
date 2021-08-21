from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from tinymce import models as tinymce_models
from datetime import datetime
# Create your models here.

class category(models.Model):
    category_feild = models.CharField(default="Others", null=False, max_length=20)
    summary_feild = models.CharField(default="", null=True, max_length=100)
    category_image =  models.ImageField(null=True, upload_to='upload', max_length=None)

    def __str__(self):
        return self.category_feild

class author(models.Model):
    author_name = models.CharField(default="Guest Author", null=False, max_length=20)
    author_img =  models.ImageField(null=True, upload_to='upload', max_length=None)
    author_email = models.EmailField(max_length=254)
    about_auth = models.CharField(default="Deny to disclose", null=False, max_length=100)

    def __str__(self):
        return self.author_name

class blogpost(models.Model):
    title= models.CharField(default="N/A", null=False, max_length=50)
    content = tinymce_models.HTMLField()
    blog_img =  models.ImageField(null=True, upload_to='upload', max_length=None)
    publish_date = models.DateField(default=datetime.today)
    blog_author = models.ForeignKey(author, on_delete=models.CASCADE)
    blog_category = models.CharField(default="Others", null=False, max_length=20)

    def __str__(self):
        return self.title

class comments(models.Model):
    comment_data = models.TextField(null=False)
    name_data = models.CharField(default="Guest", null=False, max_length=20)
    parent_post = models.ForeignKey(blogpost, related_name="post_id", on_delete=models.CASCADE)
    comment_date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.comment_data