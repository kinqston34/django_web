from django import forms
from .models import Customer,Detail

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }

        labels = {
            'name': '客戶名',
            'location': '居住地',
        }

class DetailModelForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'

        
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'line_id': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'tel': forms.TextInput(attrs={'class':'form-control','maxlength':"10"}),
            'create_time': forms.TimeInput(attrs={'class':'form-control'}),
            'suggest': forms.Textarea(attrs={'class':'form-control','maxlength':"500"}),
        }

        labels = {
            'name': '客戶名',
            'line_id': 'line ID',
            'email': 'Email',
            'tel': '電話號碼', 
            'create_time': '時間',
            'suggest': '意見',
        }

        

        