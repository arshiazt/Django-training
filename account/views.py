from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from django.views import View
from django.views.generic import CreateView, FormView

# Create your views here.

# class RegisterView(View):

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = UserRegistrationForm()
#         context = {'form':form}

#         return render(request,'account/registration.html',context=context)
        
#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
#         context = {'form':form}
#         return render(request,'account/registration.html',context=context)

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/registration.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)

# class LoginView(View):

#     def get(self,request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = LoginForm()
#         context = {'form':form}
#         return render(request,'account/login.html',context=context)

#     def post(self,request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             user = form.cleaned_data.get('user')
            
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')

#         context = {'form':form}
#         return render(request,'account/login.html',context=context)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs) 
    
    def form_valid(self, form):
        user = form.cleaned_data.get('user')

        if user is not None:
            login(self.request,user)
            return super().form_valid(form)

        return super().form_invalid(form)

@login_required(login_url='/account/login/')
def logout_view(request):
    logout(request)
    return redirect('/')