from django.db import models


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)  # 123.55
    buy = models.DecimalField(max_digits=5, decimal_places=2)  # 123.55
    cread = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=10)
    type = models.CharField(max_length=8)


class SendMailModels(models.Model):
    email_to = models.EmailField(max_length=30)
    subject = models.CharField(max_length=126)
    body = models.CharField(max_length=2056)
    create = models.DateTimeField(auto_now_add=True)

class TimePage(models.Model):
    cread = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=256)
    response_time = models.PositiveSmallIntegerField(help_text ="in seconds")

class AdPage(models.Model):
    cread = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    num = models.CharField(max_length=16)
