from django.shortcuts import render

# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
       'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)

def get_user_profile(request, username):
   user = User.objects.get(username=username)
   return render(request, 'core/user-profile.html', {"user": user})