from django.urls import path
from currency.views import RateListView
from currency.views import RateDetailsView
from currency.views import RateUpdateView
from currency.views import RateDeleteView
from currency.views import RateCreateView
from currency.views import GenPassword
from currency.views import SendMailView
from currency.views import AdView

urlpatterns = [
    path("rate-list/", RateListView.as_view(), name='rate-list-link'),
    path("rate-details/<int:pk>", RateDetailsView.as_view(), name='rate-details-link'),
    path("rate-update/<int:pk>", RateUpdateView.as_view(), name='rate-update-link'),
    path("rate-delete/<int:pk>", RateDeleteView.as_view(), name='rate-delete-link'),
    path("rate-create/", RateCreateView.as_view(), name='rate-create-link'),
    path("gen/", GenPassword.as_view(),name='gen-password-link'),
    # path("contact-us/", Contact_UsView.as_view(), name='contact-us-link'),
    path("send-mail/", SendMailView.as_view(), name='send-mail-link'),
    path("advertisment/", AdView.as_view(), name='ad-link'),
]
