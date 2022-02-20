from cProfile import Profile
# from multiprocessing import context
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# view user profile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin

# importing NewsStory model from news directory
from news.models import NewsStory

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.views import generic
from .models import CustomUser
from django.core.exceptions import PermissionDenied

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    # def saveImage(request):
    #     if request.method == "POST":
    #         image = request.FILES.get('image')
    #         new_image = <Image_Model>.objects.create(image = image
    #     )

    #     return redirect('/somewhere/')
    # return render(request, 'new_image.html',)
    

# class EditAccountView():
#     form_class = UserCha
#     success_url = reverse_lazy('login')
#     template_name = 'users/createAccount.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['all_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context
    
   
    

class UpdateProfileView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    context_object_name = 'userForm'
    template_name = 'users/updateProfile.html'
    # fields = ['email', 'about_me', 'image']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        user_id = self.object.id
        return reverse('user:profile', kwargs={'pk': user_id})

    def get_object(self, queryset = None):
        profile= super().get_object(queryset)
        if profile != self.request.user:
            raise PermissionDenied
        return profile
