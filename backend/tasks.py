from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from time import sleep
from backend.models import ConfirmEmailToken, User


@shared_task()
def send_email(title, message, email, *args, **kwargs):
    email_list = list()
    email_list.append(email)
    print(message)
    try:
        msg = EmailMultiAlternatives(
            subject=title,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=email_list
        )
        msg.send()
        # msg = EmailMultiAlternatives(subject=title, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
        # msg.send()
        # return f'{title}: {msg.subject}, Message:{msg.body}'
    except Exception as excp:
        raise excp
