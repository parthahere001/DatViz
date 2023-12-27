# your_project/urls.py

from django.urls import path
from .views import LoadDataFromJsonView, FetchDataView

urlpatterns = [
    # path('load-data/', LoadDataFromJsonView.as_view(), name='load_data'),
    path('fetch-data/', FetchDataView.as_view(), name='fetch_data'),
]
