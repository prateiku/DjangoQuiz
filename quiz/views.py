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