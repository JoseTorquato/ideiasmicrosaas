from django.db import models

class Ideas(models.Model):
    id = models.AutoField(primary_key=True)
    microsaas_name = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    how_it_works = models.TextField()
    business_model = models.TextField()
    target_audience = models.TextField()
    competitive_edge = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.microsaas_name

class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)