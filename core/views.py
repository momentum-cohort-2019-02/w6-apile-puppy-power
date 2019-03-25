from django.shortcuts import render, redirect, get_object_or_404
from core.models import PostLink, User, Vote, Comment, HashTag
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views import generic
from django.db.models import Count, Max, F

# Create your views here.
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/user_profile.html', {"user":user})

def index(request):
    """Index View"""
    PostLink.objects.all().annotate(num_comments=Count('comment')).order_by('-num_comments', '-created_at')
    model = PostLink
    postlinks = PostLink.objects.all().annotate(num_comments=Count('comment')).order_by('-num_comments', '-created_at')
    num_postlinks = PostLink.objects.all().count()

    context = {
        'postlinks' : postlinks,
        'num_postlinks' : num_postlinks,
    }

    return render(request, 'index.html', context=context)

@require_http_methods(['POST'])
@login_required
def postlink_vote_view(request, pk):
    postlink = get_object_or_404(PostLink, pk=pk)

    vote, created = request.user.vote_set.get_or_create(postlink=postlink)

    if created:
        messages.success(request, f"You have voted for {postlink.title}.")
        pass
    else:
        messages.info(request, f"You have removed your vote for {postlink.title}.")
        vote.delete()
        
    return redirect(postlink.get_absolute_url())

class PostLinkDetailView(generic.DetailView):
    model = PostLink
    paginate_by = 20


# this was our new attempt at new postdetail
# def postlink_detail_view(request, pk):
#     """Postlink detail View"""
#     postlinks = PostLink.objects.all()
#     comments = Comment.objects.all()
#     # num_comments = Comment.postlink.count

#     context = {
#         'postlinks' : postlinks,
#         'comments' : comments,
#         # 'num_comments' : num_comments,
#     }

#     return render(request, 'detail_postlink.html', context=context)

@require_http_methods(['POST'])
@login_required
def new_comment(request, pk):
    postlink = get_object_or_404(PostLink, pk=pk)

    comment, created = request.user.comment_set.get_or_create(postlink=postlink)

    return redirect(postlink.get_absolute_url())

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    postlink.delete()
    return redirect('index.html')

@login_required
def add_post(request):
    model = PostLink
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post = form.save()
            return redirect(postlink.get_absolute_url())
    
    else:
        form = PostForm()
        return render(request, 'core/add_post.html', {"form": form})





    
