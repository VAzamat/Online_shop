from django.urls import path
from dealer.views import home


from dealer.apps import DealerConfig

app_name = DealerConfig.name

urlpatterns = [
    path("", home, name='home'),
]