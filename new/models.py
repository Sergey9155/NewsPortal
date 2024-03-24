from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    rating_user = models.IntegerField(default=0)

    def update_rating(self):
        r1 = Post.rating_news#*3
        r2 = Comment.rating_comment #sum
        return r1 * 3 + r2


class Category(models.Model):
    name_category = models.TextField(unique=True)

    def __str__(self):
        return self.name_category.title()


class Post(models.Model):

    ARTICLE = 'AR'
    NEWS = 'NE'

    ARTICLE_OR_NEWS = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    ]

    author = models.ForeignKey("Author", models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    time_in = models.DateTimeField(auto_now_add=True)
    choice_news = models.CharField(max_length=2, choices=ARTICLE_OR_NEWS, default=ARTICLE)
    title_news = models.CharField(max_length=150)
    text_news = models.CharField(max_length=1500)
    rating_news = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title_news.title()}: {self.text_news[:20]}'

    def like(self):
        self.rating_news += 1

    def dislike(self):
        self.rating_news -= 1

    def preview(self):
        return len(self.text_news)[:124]


class PostCategory(models.Model):
    category = models.ForeignKey("Category", models.CASCADE)
    post = models.ForeignKey("Post", models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey("Post", models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    text_comment = models.CharField(max_length=1000)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1

    def dislike(self):
        self.rating_comment -= 1
