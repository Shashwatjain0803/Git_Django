from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('first_html/',views.first_html ,name= "first_html"),
    path('forms.html/',views.forms_html , name="forms_html"),
]