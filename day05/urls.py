
from django.urls import path,include
from day05.views import view_filter,view_lable,view_lable_s
urlpatterns = [
    path("view/",view_filter),
    path("lable/",view_lable),
    path("lable_s/",view_lable_s),
]