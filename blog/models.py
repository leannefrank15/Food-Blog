from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.

class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def tagname(self):
    return f"{self.caption}"

  def __str__(self):
    return self.tagname()


class Author(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  email = models.EmailField()

  def fullname(self):
    return f"{self.firstname} {self.lastname}"

  def __str__(self):
    return self.fullname()
  

class Post(models.Model):
  title=models.CharField(max_length=50)
  excerpt = models.CharField(max_length=250)
  image = models.ImageField(upload_to="posts", null=True)
  date = models.DateField(auto_now=True)
  slug = models.SlugField(unique=True)
  content = models.TextField(validators=[MinLengthValidator(10)])
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") #sets up one to many relationship
  tags = models.ManyToManyField(Tag)

class Comment(models.Model):
  user_name = models.CharField(max_length=100)
  user_email = models.EmailField()
  text = models.TextField(max_length=300)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

  def __str__(self):
    return f"{self.user_name}"