from cProfile import Profile
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

# view user profile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin

# importing NewsStory model from news directory
from news.models import NewsStory

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    

# class EditAccountView():
#     form_class = UserCha
#     success_url = reverse_lazy('login')
#     template_name = 'users/createAccount.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
    #     if NewsStory.objects.filter(author=self.kwargs['pk']) is not "":
    #         context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
    #     else:
    #         context['user_stories'] = "no stories available"
    #     return context

    
    
    # def profile_index(request):
    #     logged_in_user = request.Cus


# ^requires user to log in before they can access user profile.
    
    