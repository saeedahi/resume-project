from django import forms
from home.models import ContactUsModel


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'نام خود را وارد کنید',
                    'oninvalid': 'this.setCustomValidity("لطفا نام و نام خانوادگی خود را وارد کنید")',
                    'oninput': 'this.setCustomValidity("")',
                    'id': 'name',
                    'name': 'name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'ایمیل خود را وارد کنید',
                    'oninvalid': 'this.setCustomValidity("لطفا ایمیل خود را وارد کنید")',
                    'oninput': 'this.setCustomValidity("")',
                    'id': 'email',
                    'name': 'email'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'پیام خود را بنویسید',
                    'rows': 5,
                    'oninvalid': 'this.setCustomValidity("لطفا پیام خود را وارد کنید")',
                    'oninput': 'this.setCustomValidity("")',
                    'id': 'message',
                    'name': 'message',
                }
            )
        }