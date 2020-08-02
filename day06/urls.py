
from django.urls import path,include

from day04.views import if_view,for_view
urlpatterns = [
    path("view/<name>/",if_view),
]