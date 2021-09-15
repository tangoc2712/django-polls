from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question 

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:]
    # create context for html template
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "Bạn đang xem kết quả của câu hỏi %s"
    return HttpResponse(response % question_id)   

def vote(request, question_id):
    return HttpResponse("Bạn đang thực hiện vote cho câu hỏi %s" % question_id)
