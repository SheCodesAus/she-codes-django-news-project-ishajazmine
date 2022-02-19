from dataclasses import fields
from django.views import generic
from .models import NewsStory

# BELOW: FORM TUTORIAL IMPORTS
from django.urls import reverse_lazy, reverse
from .forms import StoryForm
from django.core.exceptions import PermissionDenied



class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# form class
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/createStory.html'
    fields = ['title', 'image', 'content']
    
    def get_success_url(self):
        story_id = self.object.id
        return reverse('news:story', kwargs={'pk: story_id'},
        
        )
    
# to delete story make new template. edit sotry use existing.
class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset = None):
        story= super().get_object(queryset)
        if story.author != self.request.user:
            raise PermissionDenied
        return story
        