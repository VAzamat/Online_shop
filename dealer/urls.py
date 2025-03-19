from django.urls import path
from dealer.views import index


from dealer.apps import DealerConfig

app_name = DealerConfig.name

urlpatterns = [
    path("", index, name='index'),
]
