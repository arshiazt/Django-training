from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView 


# Create your views here.

def index_view(request):
    return render(request,'web/index.html')

class IndexView(View):

    def get(self, request):
        return render(request,'web/index.html')
    
class IndexTemplateView(TemplateView):
    template_name = 'web/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = 'arshia'
    #     return context