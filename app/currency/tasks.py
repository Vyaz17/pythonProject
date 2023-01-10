import time
from decimal import Decimal

# from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def debag_task(sleep_time: int = 5):
    from time import sleep
    s = time.time()
    sleep(sleep_time)
    e = time.time()
    print(f"Task competed in {e - s}")


@shared_task
def send_mail_task(s, b, m):
    send_mail(
        "s",
        "b",
        "879846test@gmail.com",
        ["879846test@gmail.com"],
        fail_silently=False,
    )


# @shared_task
# def db_work():
#     from currency.models import Rate
#
#     print(Rate.objects.count())


@shared_task
def privat_parse():
    import requests

    privat_currency_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

    responce = requests.get(privat_currency_url)

    rates = responce.json()
    from currency.models import Rate
    source_parse = "privat"
    for i in rates:
        if i["ccy"] == "USD" or i["ccy"] == "EUR":
            currency_type_parse = i["ccy"]
            # sale_parse = i['sale']
            sale_parse = Decimal(i['sale']).quantize(Decimal('.01'))
            # buy_parse = i['buy']
            buy_parse = Decimal(i['buy']).quantize(Decimal('.01'))

            last_rate = Rate.objects.filter(
                type=currency_type_parse,
                source=source_parse
            ).order_by("cread").last()

            if last_rate is None or last_rate.sale != sale_parse or last_rate.buy != buy_parse:
                Rate.objects.create(
                    type=currency_type_parse,
                    sale=sale_parse,
                    buy=buy_parse,
                    source=source_parse,
                )


@shared_task
def minfin_parse():
    import requests

    privat_currency_url = "https://minfin.com.ua/currency/"

    responce = requests.get(privat_currency_url)
    from currency.models import Rate
    source_parse = "minfin"
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(responce.text, "html.parser")

    mf_type = soup.find("td", {"class": "mfcur-table-cur"}).text.split("\n")
    mf_type = mf_type[1]

    mf_usd_buy = soup.find("td", {"class": "mfm-text-nowrap"}).text.split("\n")
    mf_usd_buy = mf_usd_buy[1].replace(",", ".")
    mf_usd_buy = Decimal(mf_usd_buy).quantize(Decimal('.01'))

    mf_usd_sale = soup.find("td", {"class": "mfm-text-nowrap"}).text.split("\n")
    mf_usd_sale = mf_usd_sale[-2].replace(",", ".")
    mf_usd_sale = Decimal(mf_usd_sale).quantize(Decimal('.01'))

    Rate.objects.create(
        type=mf_type,
        sale=mf_usd_sale,
        buy=mf_usd_buy,
        source=source_parse,
    )


# from currency.models import SendMailModels
# from django.urls import reverse_lazy


@shared_task
def send_mail():
    from django.core.mail import send_mail
    send_mail(
        'Subject here',
        'Here is the message.',
        '879846test@gmail.com',
        ['879846test@gmail.com'],
        fail_silently=False,
    )
