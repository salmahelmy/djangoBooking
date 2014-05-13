from django.shortcuts import render
#from users.models import User
#from users.models import UserForm
from users.forms import UserForm
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        #context = {'formData':form}
        if form.is_valid():
            cd = form.cleaned_data
            newUser=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            newUser.first_name=cd['firstname']
            newUser.last_name=cd['lastname']
            newUser.save()
            return render(request, 'users/register.html', {'newUser':form})
        else:
            return render(request, 'users/register.html', {'newUser':form})
    else:
        form = UserForm()
        context = {'formData':form}
    return render(request, 'users/register.html', {'newUser':form})

def signIn(request):
    if request.method == 'POST':
        form = UserForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            # Redirect to a success page.
                    return HttpResponse("Hello user")
                else:
                    return HttpResponse("not active")
            else:
        # Return an 'invalid login' error message.
                return HttpResponse("not registered")
    else:
        form = UserForm()
        return render(request, 'users/signin.html',{'newUser':form})
    
'''def logout_view(request):
    logout(request)'''
        
        
           

