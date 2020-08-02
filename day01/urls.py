from django.urls import path ,re_path
from day01.views import view_fun,view_re_fun,view_fun2,templates,view_templ,view_temp2,view_temp3
from day01.views import form_reg

urlpatterns = [
   path("view/name/",view_fun,name='v0'),
   path("view/v1/",view_fun2,name='v1'),
   re_path("^2\d{2,3}$",view_re_fun),
   path("form/",templates),
   path("form2/",view_templ),
   path("demo_v2/",view_temp2),
   path("sorty/",view_temp3),
   path("reg/", form_reg),
]