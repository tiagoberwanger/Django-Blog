from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('contato/', views.contato, name='contato'),
    path("<slug:slug>/", views.PostDetailView.as_view(), name='detail'),

]
