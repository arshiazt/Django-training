from django.shortcuts import render
from .forms import ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.

class ProfileEditView(LoginRequiredMixin,UpdateView):
    template_name = 'user/profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile')
    login_url = '/account/login/'

    def get_object(self, queryset=None):
        return self.request.user.profile