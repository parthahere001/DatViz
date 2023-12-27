import json
import os
import django
from django.core.management import settings
from mainapp.models import ArticleData
from mainapp.serializers import ArticleDataSerializer

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datvizbackend.settings")

# Configure Django settings
django.setup()

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        for item in data:
            # Convert string representations of dates to datetime objects
            item['added'] = datetime.datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S') if item['added'] else None
            item['published'] = datetime.datetime.strptime(item['published'], '%B, %d %Y %H:%M:%S') if item['published'] else None

            # Use the serializer to validate and create the model instance
            serializer = ArticleDataSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in data: {serializer.errors}")

if __name__ == "__main__":
    import datetime
    file_path = "jsondata.json"  # Replace with the actual path to your JSON file
    load_data_from_json(file_path)
