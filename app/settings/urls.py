from django.contrib import admin
from django.urls import path, include
from currency.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name='index-link'),

    path('rate/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('api/', include('API.urls')),

    # # API
    # path("rates_list_api_example/", rates_list_api_example)
]
