from django import forms
from .models import Products, OSA, Technicals, Documents, Modifications, Connectors, Orders, Request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя и фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    contact = forms.CharField(label='Контакты для связи', widget=forms.TextInput(attrs={'class': 'form-control'}))



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['serial_num', 'modification', 'con_type', 'create_date', 'order']
        widgets = {
            'serial_num': forms.TextInput(attrs={'class': 'form-control'}),
            'modification': forms.Select(attrs={'class': 'form-select'}),
            'con_type': forms.Select(attrs={'class': 'form-select'}),
            'create_date': forms.DateInput(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-select'}),
        }


class OSAForm(forms.ModelForm):
    class Meta:
        model = OSA
        fields = ['serial_num', 'gain', 'gain_flatness', 'noise_figure']
        widgets = {
            'serial_num': forms.Select(attrs={'class': 'form-select'}),
            'gain': forms.TextInput(attrs={'class': 'form-control'}),
            'gain_flatness': forms.TextInput(attrs={'class': 'form-control'}),
            'noise_figure': forms.TextInput(attrs={'class': 'form-control'})
        }


class TechnicalForm(forms.ModelForm):
    class Meta:
        model = Technicals
        fields = ['serial_num', 'i_op', 'i_eol', 'p_op', 'p_eol', 'attenuation']
        widgets = {
            'serial_num': forms.Select(attrs={'class': 'form-select'}),
            'i_op': forms.TextInput(attrs={'class': 'form-control'}),
            'i_eol': forms.TextInput(attrs={'class': 'form-control'}),
            'p_op': forms.TextInput(attrs={'class': 'form-control'}),
            'p_eol': forms.TextInput(attrs={'class': 'form-control'}),
            'attenuation': forms.TextInput(attrs={'class': 'form-control'})
        }


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['serial_num', 'laser', 'passtopt']
        widgets = {
            'serial_num': forms.Select(attrs={'class': 'form-select'}),
            'laser': forms.FileInput(attrs={'class': 'form-control'}),
            'passtopt': forms.FileInput(attrs={'class': 'form-control'})
        }


class ModificationForm(forms.ModelForm):
    class Meta:
        model = Modifications
        fields = ['mod']
        widgets = {
            'mod': forms.TextInput(attrs={'class': 'form-control'})
        }


class ConnectorForm(forms.ModelForm):
    class Meta:
        model = Connectors
        fields = ['type']
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['order']
        widgets = {
            'order': forms.TextInput(attrs={'class': 'form-control'})
        }


class ReqForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['count', 'count_m12', 'count_n19', 'con_type', 'req_date', 'end_of_date', 'order', 'explanations']
        widgets = {
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'count_m12': forms.TextInput(attrs={'class': 'form-control'}),
            'count_n19': forms.TextInput(attrs={'class': 'form-control'}),
            'con_type': forms.Select(attrs={'class': 'form-select'}),
            'req_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_of_date': forms.DateInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'explanations': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
