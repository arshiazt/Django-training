from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # list profile
    path('profile/list/',views.ProfileListView.as_view(),name='profile-list'),
    # profile edit
    path('profile/edit/',views.ProfileEditView.as_view(),name='profile-edit'),
    # profile detail
]