from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template import loader
from .models import Profile


@login_required(login_url='signin')
def index(request):
  # template = loader.get_template('index.html')
  # return HttpResponse(template.render())
  return render(request, 'index.html')

@login_required(login_url='signin')
def settings(request):
  user_profile = Profile.objects.get(user = request.user)

  if request.method =='POST':
    if request.FILES.get('image') == None:
      image = user_profile.profileimg
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()

    if request.FILES.get('image') != None:
      image = request.FILES.get('image') 
      bio = request.POST['bio']
      location = request.POST['location']

      user_profile.profileimg = image
      user_profile.bio = bio
      user_profile.location = location
      user_profile.save()
    return redirect('setting')  

  return render(request, 'setting.html', {'user_profile': user_profile})

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username= username, password=password)

    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request, "fail")
      return redirect('signin')
  
  else:
    return render(request, 'signin.html')

def signup(request):

  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, "Email taken")
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, "Username taken")
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user_login = auth.authencation(username=username, password = password)
        auth.login(request, user_login)
        print(user)

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')

    else:
      messages.info(request, "Password not matching")
      return redirect('signup')
    
  else:
    return render(request, 'signup.html')
  
@login_required(login_url='signin')  
def logout(request):
  auth.logout(request)
  return redirect(signin)