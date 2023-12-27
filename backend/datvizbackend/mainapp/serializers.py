
from rest_framework import serializers
from .models import ArticleData

class ArticleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleData
        fields = '__all__'

    def to_internal_value(self, data):
        # Convert empty strings to None for fields that should be integers
        for key in ['end_year', 'start_year', 'impact', 'intensity', 'likelihood', 'relevance', 'added', 'published']:
            if key in data and data[key] == "":
                data[key] = None

        return super().to_internal_value(data)
