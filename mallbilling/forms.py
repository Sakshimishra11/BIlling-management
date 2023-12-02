# mallbilling/forms.py

from django import forms
from .models import Admin,Product,Employee,Customer




class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['admin','first_name','last_name','employee_id','password']

class AdminCreationForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['admin_id', 'password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']


 

        
              
            