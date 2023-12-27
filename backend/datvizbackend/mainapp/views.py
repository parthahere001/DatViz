from django.shortcuts import render

import json
import datetime
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from .models import ArticleData
from .serializers import ArticleDataSerializer

class LoadDataFromJsonView(View):
    def get(self, request, *args, **kwargs):
        file_path = "mainapp/jsondata.json"  # Replace with the actual path to your JSON file

        try:
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
                        # Handle validation errors
                        return JsonResponse({'error': f"Error in data: {serializer.errors}"}, status=400)

            return JsonResponse({'success': 'Data loaded successfully'}, status=200)

        except FileNotFoundError:
            return JsonResponse({'error': 'File not found'}, status=404)

        except ValidationError as e:
            return JsonResponse({'error': f"Validation error: {e}"}, status=400)

        except Exception as e:
            return JsonResponse({'error': f"An unexpected error occurred: {e}"}, status=500)
