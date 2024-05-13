from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Search, Poll, Answer


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:15]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Вы не сделали выбор.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def search(request):
    search_query = request.GET.get('search_query', '')
    search_results = Question.objects.filter(question_text__icontains=search_query)
    return render(request, 'polls/search.html', {'search_results': search_results, 'search_query': search_query})

def create_poll(request):
    if request.method == 'POST':
        poll_title = request.POST.get('poll_title')
        new_poll = Poll.objects.create(title=poll_title)
        
        answer_options = request.POST.getlist('answer_option')
        for option in answer_options:
            Answer.objects.create(poll=new_poll, option=option)
        
        return HttpResponseRedirect('/success/')

    return render(request, 'polls/create.html')

def success_page(request):
    return render(request, 'polls/success.html')