from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from handyman.models import MasterTasks, Feedbacks, Master, PortfolioImage


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            normal_user_group = Group.objects.get(name='user')
            user.groups.add(normal_user_group)
        return user


class MasterTasksForm(forms.ModelForm):
    class Meta:
        model = MasterTasks
        fields = ['master_type', 'client_name', 'client_tel', 'client_adders']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['feedback']


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'skill', 'workarea', 'image', 'experience']


class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image']
