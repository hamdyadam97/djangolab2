from django import forms
from .models import Trainee
The_Choices ={
    ('f','female'),
    ('m','male')
}


class InsertForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput)
    national_num = forms.IntegerField()
    sex = forms.ChoiceField(choices=The_Choices)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'




