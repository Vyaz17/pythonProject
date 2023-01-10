from django.urls import path
from accounts.views import MyProfileView
from accounts.views import SingUpView
from accounts.views import ActivateUpView

app_name = 'accounts'

urlpatterns = [
    path("my-profile/<int:pk>", MyProfileView.as_view(), name='my-profile'),
    path('sing-up/',SingUpView.as_view(), name='sing-up-link' ),
    path('/activate/<uuid:username>/',ActivateUpView.as_view(), name='activate-link' ),

]
