from django.urls import path
from API.views import API_Rate_View
from API.views import API_Rate_Details_View

urlpatterns = [
    path("retes/", API_Rate_View.as_view(), name="api-link"),
    path("retes/<int:pk>/", API_Rate_Details_View.as_view(), name="api-link"),
]
