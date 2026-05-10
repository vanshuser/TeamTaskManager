from django import forms
from .models import Task
from django.utils.timezone import now

class TaskForm(forms.ModelForm):


    
    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'project',
            'assigned_to',
            'deadline',
            'status',
            'priority'
        ]
        widgets = {
    'deadline': forms.DateInput(
        attrs={'type': 'date'}
    )
}

    def clean_deadline(self):

            deadline = self.cleaned_data['deadline']

            if deadline < now().date():

                raise forms.ValidationError(
            "Deadline cannot be in the past."
        )

            return deadline

