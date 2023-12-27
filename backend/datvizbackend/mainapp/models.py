from django.db import models
from rest_framework import serializers



class ArticleData(models.Model):
    end_year = models.PositiveSmallIntegerField(blank=True, null=True)
    intensity = models.FloatField(blank=True, null=True)
    sector = models.TextField(null=True, blank=True)
    topic = models.TextField(null=True, blank=True)
    insight = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True, max_length=20000)
    region = models.TextField(null=True, blank=True)
    start_year = models.PositiveSmallIntegerField(blank=True, null=True)
    impact = models.IntegerField(blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    relevance = models.PositiveSmallIntegerField(blank=True, null=True)
    pestle = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    likelihood = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.published.strftime('%B, %d %Y %H:%M:%S') if self.published else 'N/A'}"








