from django.core.mail import send_mail


def activate_email(activation_linc, email_to):
    subject = "cсылка активации"

    body = f" hi! your link: {activation_linc}"

    send_mail(
        subject,
        body,
        '879846test@gmail.com',
        [email_to],
        fail_silently=False,
    )