from django.http import HttpResponse
from sendmail import settings
from django.core.mail import send_mail


def mail(request):
    subject = "Greetings from shubham"
    msg     = "hey shubham how are you "
    to      = "shubham.conceptualise@gmail.com"
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfulys"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)

# Create your views here.
