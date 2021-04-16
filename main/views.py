from django.shortcuts import redirect, render
from .models import Question
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    if request.POST:
        question = request.POST['question']
        hint = request.POST['hint']
        answer = request.POST['answer']
        subject = request.POST['subject']
        new_question = Question(auther=request.user, question=question, hint=hint, answer=answer, subject=subject)
        new_question.save()
        return redirect('home')
    questions = Question.objects.all().order_by('-timestamp')
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    context = {'questions':questions}
    return render(request, 'main/index.html', context)

def search(request):
    if request.GET:
        query = request.GET['q']
        questions = Question.objects.filter(question__icontains=query) | Question.objects.filter(subject__icontains=query)
        paginator = Paginator(questions, 10)
        page = request.GET.get('page')
        questions = paginator.get_page(page)
        context = {'questions':questions}
        return render(request, 'main/search.html', context)
    return redirect('home')