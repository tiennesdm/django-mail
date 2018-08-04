from django.conf.urls import url,include
from .views import mail


urlpatterns = [
url(r'^mail',mail ),
]
