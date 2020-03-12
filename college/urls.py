from . import views
from django.urls import path

urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('index/', views.index),
    path('upload/',views.upload),
    path('upload/usingupload/',views.uploadimage),
    path('upload/usinglink/',views.link),
    path('upload/usinglinkpdf/',views.linkpdf),
    path('index/upload/delete/<int:dl>/',views.delete),
    path('select/delete/<int:cdl>/<slug:topic>/',views.cdelete),
    path('newcategory/',views.newcat),
    path('selectcard/',views.card),
    path('selectcard/<slug:tp>/',views.selectcard)
]
