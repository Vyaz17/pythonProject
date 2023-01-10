from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from accounts.models import User
from accounts.SingUpForm import SingUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import RedirectView


class MyProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ("first_name", "last_name")
    success_url = reverse_lazy('index-link')
    template_name = "my_profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


class SingUpView(CreateView):
    model = User
    template_name = 'sing_up.html'
    form_class = SingUpForm
    success_url = reverse_lazy('index-link')

    def form_valid(self, form):
        from django.contrib import messages
        messages.info(self.request, "спасибо!")
        return super().form_valid(form)


class ActivateUpView(RedirectView):
    pattern_name = 'index-link'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop("username")
        user = get_object_or_404(User, username=username, is_active=False)
        user.is_active = True

        from django.contrib import messages
        user.save(update_fields=('is_active',))
        messages.info(self.request, 'Your accaunts is activated')

        user.refresh_from_db()
        return super().get_redirect_url(*args, **kwargs)
