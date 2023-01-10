# import settings.settings
from currency.models import Rate
from currency.models import SendMailModels
from currency.forms import RateForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
# from django.views.generic import View
# from django.http import HttpResponse
from django.urls import reverse_lazy
from currency.utils import gen_password


class HomeView(TemplateView, ):
    template_name = "index.html"


class Page2View(TemplateView):
    template_name = "page2.html"


class RateListView(ListView):
    # queryset = Rate.objects.all()
    model = Rate
    template_name = 'rateList.html'

    # def get(self, request, *args, **kwargs):
    #     print("*"*10)
    #     print(request.COOKIES)
    #     print("*" * 10)
    #     return super().get(request, *args, **kwargs)


class RateDetailsView(DetailView):
    model = Rate
    template_name = "rateDetails.html"


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list-link')
    template_name = "rateUpdate.html"


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate-list-link')
    template_name = "rateDelete.html"


class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list-link')
    template_name = "rateCreate.html"


class GenPassword(TemplateView):
    template_name = 'gen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            password_len = int(self.request.GET.get('pl'))
        except TypeError:
            password_len = 10

        context['password1'] = gen_password(password_len)  # 1234567890duas

        return context


class SendMailView(CreateView):
    model = SendMailModels
    fields = (
        "email_to",
        "subject",
        "body",
    )
    success_url = reverse_lazy('index-link')
    template_name = "Send_mail.html"

    def form_invalid(self, form):
        print("форма не корректна")
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        from currency.tasks import send_mail_task
        # s = form.cleaned_data['subject']
        send_mail_task.delay(form.cleaned_data['subject'], form.cleaned_data['body'], form.cleaned_data['email_to'])
        # send_mail_task.apply_async(args=(form.cleaned_data['subject'],form.cleaned_data['body'],form.cleaned_data['email_to']))
        return super().form_valid(form)


# def rates_list_api_example(request):
#     import json
#     rates = Rate.objects.all()
#     result = []
#     for i in rates:
#         result.append(
#             {
#                 "id": i.id,
#                 "type": i.type,
#                 "buy": float(i.buy),
#                 "sale": float(i.sale),
#             }
#         )
#
#     return HttpResponse(json.dumps(result), content_type="application/json")


class AdView(TemplateView):
    template_name = "ad.html"
