from django.shortcuts import render
from .forms import ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView
from .models import Profile

# Create your views here.

class ProfileEditView(LoginRequiredMixin,UpdateView):

    template_name = 'user/profile_edit.html'
    form_class = ProfileEditForm
    login_url = '/account/login/'
    success_url = reverse_lazy('user:profile-edit')
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
class ProfileListView(ListView):

    # model = Profile
    queryset = Profile.objects.filter(user__is_active=True)
    template_name = 'user/profile_list.html'
    context_object_name = 'profiles'

    # def get_queryset(self):
    #     return Profile.objects.filter(
    #     user__is_active=True
    # ).exclude(
    #     user=self.request.user
    # )

class ProfileDetailView(DetailView):

    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'
    model = Profile
    pk_url_kwarg = 'id'