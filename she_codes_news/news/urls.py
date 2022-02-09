from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # ^^what does this mean - primary key
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
]
