from django import forms
from . import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeInfo
        fields = ['fullname','Employee_code','address','birth','position']
        labels = {
            'Employee_code': 'Employee Code',
            'birth':'Date of Birth'
        }

    def __init__(self, *args ,**kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select Position'