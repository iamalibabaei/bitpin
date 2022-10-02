from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    score_count = models.PositiveBigIntegerField()
    score_sum = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title


class PostScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_post_user')
        ]

    def __str__(self):
        return self.post.title + " " + str(self.score)
