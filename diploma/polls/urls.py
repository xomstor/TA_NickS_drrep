from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/question_id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/question_id/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/question_id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/question_id/search/
    path('search/', views.search, name='search'),
    path('create/', views.create_poll, name='create'),
    path('success/', views.success_page, name='success'),
]
