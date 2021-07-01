from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/',  views.dashboard, name="dashboard"),
    path('addarticle/',  views.addarticle, name="addarticle"),
    path('article/<int:id>',  views.details, name="detail"),
    path('update/<int:id>',  views.updateArticle, name="update"),
    path('delete/<int:id>',  views.deleteArticle, name="delete"),
    path('comment/<int:id>',  views.addComment, name="comment"),
    path('',  views.articles, name="articles"),
]