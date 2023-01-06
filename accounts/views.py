from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from.forms import RegistrationForm


# Create your views here.
def RegistrationView(request):
    form =RegistrationForm()
    if request.method =='POST':
        paswd=request.POST['password1']
        form =RegistrationForm(request.POST)
         
        if form.is_valid():
            user = form.save(commit=False)
            print('add',user.password)
            # Todo implement email activation
            user.email= user.email.strip().lower()
            user.is_active =True
            user.save()
            my_group = Group.objects.get(name='View Only') 
            my_group.user_set.add(user)
            user = authenticate(request, email=user.email, password=paswd)
            login(request, user)
            return redirect('/insight/dashboard')



    context={
        'form':form
        }


    return render(request,'accounts/register.html',context)



