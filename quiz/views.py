from django.shortcuts import redirect, render
from .forms import ExamForm
from .forms import Exam

# Create your views here.
def home(request):
    exam = Exam.objects.all()
    score = 0
    print(id)
    """ user_inputs = request.POST.items() # key: choice<question_no> and value: <user_choice>
    for question in exam:
        user_choice = user_inputs.get(question.id)
        if user_choice == question.answer1:
            score+=1 """
    return render(request, 'index.html', {'exam':exam,'score': score})


 
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = ExamForm()
    return render(request, 'create.html', {'form': form})