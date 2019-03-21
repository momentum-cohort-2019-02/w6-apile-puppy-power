import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods

from .models import PostLink, HashTag, Comment, Vote

# Create your views here.
def index(request):
    postlinks = PostLink.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'postlinks' : postlinks,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)

@login_required
@require_POST

class PostLinkCreateView(generic.CreateView):
    model = PostLink
    fields = ('title', 'author', 'description', 'post_url')

class PostLinkDetailView(generic.DetailView):
    model = PostLink

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')
