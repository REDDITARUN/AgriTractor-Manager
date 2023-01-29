from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Tractor
from .forms import TractorForm

# Create your views here.


@login_required(login_url='login')
def index(request):
  return render(request, 'tractors/index.html', {
    'tractors': Tractor.objects.all()
  })

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'tractors/signup.html', {
    'tractors': Tractor.objects.all()
  })

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    
    return render (request,'tractors/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def view_tractor(request, id):
  tractor = Tractor.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = TractorForm(request.POST)
    if form.is_valid():
      new_tractor_id = form.cleaned_data['tractor_id']
      new_model_name = form.cleaned_data['model_name']
      new_owner_name = form.cleaned_data['owner_name']
      new_email = form.cleaned_data['email']
      new_field_Implements = form.cleaned_data['field_Implements']
      new_used_by = form.cleaned_data['used_by']

      new_tractor = Tractor(
        tractor_id = new_tractor_id,
        model_name = new_model_name,
        owner_name = new_owner_name,
        email = new_email,
        field_Implements = new_field_Implements,
        used_by = new_used_by
      )
      new_tractor.save()
      return render(request, 'tractors/add.html', {
        'form': TractorForm(),
        'success': True
      })
  else:
    form = TractorForm()
  return render(request, 'tractors/add.html', {
    'form': TractorForm()
  })



def edit(request, id):
  if request.method == 'POST':
    tractor = Tractor.objects.get(pk=id)
    form = TractorForm(request.POST, instance=tractor)
    if form.is_valid():
      form.save()
      return render(request, 'tractors/edit.html', {
        'form': form,
        'success': True
      })
  else:
    tractor = Tractor.objects.get(pk=id)
    form = TractorForm(instance=tractor)
  return render(request, 'tractors/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    tractor = Tractor.objects.get(pk=id)
    tractor.delete()
  return HttpResponseRedirect(reverse('index'))