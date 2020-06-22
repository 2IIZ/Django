from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' #or you can just ('fullname', 'emp_code',...)
        labels = {
            'fullname':'Full Name',
            'emp_code':'Your Code',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label  = "Select"
        self.fields['emp_code'].required = False