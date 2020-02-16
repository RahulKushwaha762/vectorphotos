from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('upload/',views.upload),
    path('upload/usingupload/',views.uploadimage),
    path('upload/usinglink/',views.link),
    path('upload/delete/<int:dl>/',views.delete),
    path('newcategory/',views.newcat)
]