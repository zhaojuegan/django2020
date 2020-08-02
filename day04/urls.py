
from django.urls import path,include

from day04.views import if_view,for_view,base_view
urlpatterns = [
    path("view/<name>/",if_view),
    path("view_for/<name>/",for_view),
    path("base_view/",base_view),
]