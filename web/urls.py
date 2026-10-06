from django.urls import path
from . import views
# from django.views.generic import TemplateView, RedirectView

app_name = 'web'

urlpatterns = [
    path('',views.IndexTemplateView.as_view(),name='index'),
    # path('',TemplateView.as_view(template_name='web/index.html'),name='index'),
    # path('daneshkar/',RedirectView.as_view(url='https://daneshkar.net/'))
]