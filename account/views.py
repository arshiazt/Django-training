from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    form = UserRegistrationForm()
    context = {'form':form}
    return render(request,'account/registration.html',context=context)