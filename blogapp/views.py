from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


def contato(request):
    return render(request, 'blogapp/contato.html')
