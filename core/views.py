from django.shortcuts import render

# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
       'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)

@login_required
@require_POST

@login_required
def add_post(request):
    form_class = PostForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home",)
    
    else:
        form = form_class()
        return render(request, 'post/add_post.html', {"form": form, })

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')
