from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import School

from .models import User

# schools = School.objects.all()


class StudentSignUpForm(UserCreationForm):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(), required=True, to_field_name="name", empty_label="Select your School ▼")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['school', 'username', 'email', 'password1',
                  'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password'})
        self.fields['school'].widget.attrs.update(
            {'class': 'form-dropdown'})
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(), required=True, to_field_name="name", empty_label="      Select your School ▼")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['school', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat password'})
        self.fields['school'].widget.attrs.update(
            {'class': 'form-dropdown'})
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
