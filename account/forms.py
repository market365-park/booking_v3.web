# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm, ReadOnlyPasswordHashField
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
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '사번을 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
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
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Password confirmation', 'required': 'true',
            }
        )
    )

    email = forms.EmailField(
        label="Firm E-mail",
        widget=forms.EmailInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Kim.KIA@hyundai.com',
                'required': 'true',
            }))

    first_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '본인의 이름을 한글로 입력해 주세요.',
                'required': 'true',
            }))

    last_name = forms.ChoiceField(
        label="Team",
        choices=TEAM_NAME_CHOICES,
        widget=forms.Select(
            attrs={
#                'choice class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'select class': 'selectpicker col-md-12 col-lg-12 col-sm-12 col-xs-12',
                'data-style' : 'btn-last_name',
                'required': 'true',
            }
        )
    )

    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '회사전화 뒤 4자리를 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '사번을 입력해 주세요.',
                'required': 'true',
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Password',
                'required': 'true',
            }
        )
    )

    email = forms.EmailField(
        label="Firm E-mail",
        widget=forms.EmailInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Kim.KIA@hyundai.com',
                'required': 'true',
            }))

    first_name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '본인의 이름을 한글로 입력해 주세요.',
                'required': 'true',
            }))

    last_name = forms.ChoiceField(
        label="Team",
        choices=TEAM_NAME_CHOICES,
        widget=forms.Select(
            attrs={
#                'choice class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'select class': 'selectpicker col-md-12 col-lg-12 col-sm-12 col-xs-12',
                'data-style' : 'btn-last_name',
                'required': 'true',
            }
        )
    )

    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': '회사전화 뒤 4자리를 입력해 주세요.',
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
        # label="Username",
        max_length=30,
        regex=r'^[\w.@+-]+$',
        widget = forms.TextInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Whats your username',
                'required': 'true',
            }
        )
    )

    password = forms.CharField(
        # label="Password",
        error_messages={'invalid': "올바르지 않은 아이디 또는 패스워드 입니다."},
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Whats your password',
                'required': 'true',
            }
        )
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
#        label="Old Password",
#        help_text="Enter the old password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Enter the old password',
                'required': 'true',
            }
        )
    )

    new_password1 = forms.CharField(
#        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Enter the new password',
                'required': 'true',
            }
        )
    )

    new_password2 = forms.CharField(
 #       label="Password confirmation",
 #       help_text="Enter the same password as above, for verification.",
        widget=forms.PasswordInput(
            attrs={
                'class': 'col-md-6 col-lg-6 col-sm-6 col-xs-12',
                'placeholder': 'Repeat the new password',
				'required': 'true',
            }
        )
    )
