from django.shortcuts import redirect, render
from .forms import ExamForm
from .forms import Exam
from django.contrib import messages

# Create your views here.
def home(request):
    exam = Exam.objects.all()
    return render(request, 'index.html', {'exam':exam})


 
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Question submitted successfully")
            return redirect('create')
    else:
        form = ExamForm()
    return render(request, 'create.html', {'form': form})


def DeleteQues(request):
    numba = Exam.objects.all()
    ids = numba.values_list('QuestionNo', flat=True)
    if request.method == 'POST':
        form = ExamForm(request.POST)
        QuesNo = request.POST.get('QuestionNo')
        #print(type(QuesNo))
        if int(QuesNo) in list(ids):
            deleteQuest = Exam.objects.get(QuestionNo = QuesNo)
            deleteQuest.delete()
            messages.success(request,"Question Deleted successfully")
        else:
            messages.warning(request,"Question not found!!!")
    else:
        form = ExamForm()
    return render(request, 'delete.html', {'form': form})