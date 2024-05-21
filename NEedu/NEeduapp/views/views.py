from django.shortcuts import render
from NEeduapp.models import Course
from django.shortcuts import HttpResponse
from django.views.generic import ListView

# Create your views here.
# def index(request):
#     courses=Course.objects.all()
#     print(courses)
  
#     return render(request,template_name='homepage.html',
#     context={"courses": courses})
    
class aboutPageView(ListView):
    template_name = "about.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'about'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context

class coursesPageView(ListView):
    template_name = "courses.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context
        
    



class contactPageView(ListView):
    template_name = 'contact.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context
        

def testimonial(request):
    
     return render(request,'testimonial.html')
 
from django.shortcuts import render
from NEeduapp.models import Course
from django.shortcuts import HttpResponse
from django.views.generic import ListView

# Create your views here.
# def index(request):
#     courses=Course.objects.all()
#     print(courses)
  
#     return render(request,template_name='homepage.html',
#     context={"courses": courses})
    
class aboutPageView(ListView):
    template_name = "about.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'about'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context

class coursesPageView(ListView):
    template_name = "courses.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context
        
    



class contactPageView(ListView):
    template_name = 'contact.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context
        


class testimonialPageView(ListView):
    template_name = 'testimonial.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context
        
