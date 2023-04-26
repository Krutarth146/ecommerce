from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

# Create your views here.
def Register(request):
    # msg = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form' : form}

        if form.is_valid():
            user = form.save()
            created = True
            login(request, user)
            username = request.POST.get('username')
            customer = User.get_customer_by_username(username)
            context = {'created' : created}
            
            return redirect('/user/login')
        
        else:
            return render(request, 'user/register.html',context)
        
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'user/register.html', context)


class Login(View):
    def get(self,request):
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, authenticated_user)
                username = request.POST.get('username')
                customer = User.get_customer_by_username(username)
                request.session['customer_id'] = customer.id
                request.session['username'] = customer.username
                print(customer)
                
                return redirect('index')
            else:
                return render(request, 'user/login.html', {'form':form})
        return render(request, 'user/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('/user/login')