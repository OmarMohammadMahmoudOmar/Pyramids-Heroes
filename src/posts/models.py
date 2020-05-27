from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self): return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self): return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self): return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)


class ArticleView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=60)
    title_ar = models.CharField(max_length=60)
    overview = models.TextField(max_length=120)
    overview_ar = models.TextField(max_length=120)
    content = HTMLField()
    content_ar = HTMLField()
    thumbnail = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_feautred = models.BooleanField(default=False)
    is_english = models.BooleanField(default=False)
    @property
    def comments(self):
        return self.Comments.all()

    @property
    def view_count(self):
        return ArticleView.objects.filter(article=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(article=self).count()

    def __str__(self): return self.title + ' vs. ' + self.title_ar


class Subscribe(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.email
