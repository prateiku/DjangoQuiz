# import form class from django
from django import forms
  

from .models import Exam
  
# create a ModelForm
class ExamForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Exam
        fields = "__all__"