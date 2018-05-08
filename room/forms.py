# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm, ReadOnlyPasswordHashField

from .models import RoomBooking
from account.models import User

TEAM_NAME_CHOICES = (
    ('팀을 선택해 주세요', '팀을 선택해 주세요'),
    ('빅데이터기획팀', '빅데이터기획팀'),
    ('데이터분석1팀', '데이터분석1팀'),
    ('데이터분석2팀', '데이터분석2팀'),
    ('카클라우드개발1팀', '카클라우드개발1팀'),
    ('카클라우드개발2팀', '카클라우드개발2팀'),
    ('커넥티비티품질검증팀', '커넥티비티품질검증팀'),
    ('커넥티비티사업팀','커넥티비티사업팀'),
    ('커넥티비티1팀','커넥티비티1팀'),
    ('커넥티비티2팀','커넥티비티2팀'),
    ('차량지능화사업부','차량지능화사업부'),
    ('고객안전전략실','고객안전전략실'),
    ('전자통합개발팀','전자통합개발팀'),
)


class RegisterForm(UserCreationForm):
    username = forms.RegexField(
        label="Employee number(login ID)",
        max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and " "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and " "@/./+/-/_ characters."},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사번을 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'true',
            }
        )
    )

    password2 = forms.CharField(
        label="Password confirmation",
        help_text="Enter the same password as above, for verification.",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation', 'required': 'true',
            }
        )
    )

    email = forms.EmailField(
        label="Firm E-mail",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kim.KIA@hyundai.com',
                'required': 'true',
            }))

    first_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '본인의 이름을 한글로 입력해 주세요.',
                'required': 'true',
            }))

    last_name = forms.ChoiceField(
        label="Team",
        choices=TEAM_NAME_CHOICES,
        widget=forms.Select(
            attrs={
                'choice class': 'form-control',
                'required': 'true',
            }
        )
    )

    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '회사전화 뒤 4자리를 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone")


class ProfileUpdateForm(UserChangeForm):
    username = forms.RegexField(
        label="Employee number(login ID)",
        max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and " "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and " "@/./+/-/_ characters."},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사번을 입력해 주세요.',
                'required': 'true',
                'readonly': 'readonly'
            }
        )
    )

    email = forms.EmailField(
        label="Firm E-mail",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kim.KIA@hyundai.com',
                'required': 'true',
            }
        )
    )

    first_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '본인의 이름을 한글로 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    last_name = forms.ChoiceField(
        label="Team",
        choices=TEAM_NAME_CHOICES,
        widget=forms.Select(
            attrs={
                'choice class': 'form-control',
                'required': 'true',
            }
        )
    )

    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '회사전화 뒤 4자리를 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    password = ReadOnlyPasswordHashField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
                'required': 'true',
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email", "phone")

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyLoginForm(AuthenticationForm):
    username = forms.RegexField(
        label="Username",
        max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages = { 'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters." },
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사번',
                'required': 'true',
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
                'required': 'true',
            }
        )
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        help_text="Enter the old password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Old Password',
                'required': 'true',
            }
        )
    )

    new_password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New Password',
                'required': 'true',
            }
        )
    )

    new_password2 = forms.CharField(
        label="Password confirmation",
        help_text="Enter the same password as above, for verification.",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation', 'required': 'true',
            }
        )
    )


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')


class RoomCreateForm(forms.ModelForm):
    title = forms.CharField(
        label="Name(Team, Phone)",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    start_time = forms.CharField(
        label="Start Time",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    end_time = forms.CharField(
        label="End Time",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    room_id = forms.CharField(
        label="Meeting Room",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    class Meta:
        model = RoomBooking
        fields = ("title", "start_time", "end_time", "room_id")
