from django import forms

from bookstore.models import BookStore

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del empleado",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employee-name",
                "placeholder": "Nombre del empleado",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del empleado",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "emplyee-last-name",
                "placeholder": "Nombre del empleado",
                "required": "True",
            }
        ),
    )
    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employee-birth-date",
                "placeholder": "Fecha de nacimiento",
                "required": "True",
            }
        ),
    )
    adress = forms.CharField(
        label="Direccion del empleado",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employee-adress",
                "placeholder": "Direccion del empleado",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Student
        fields = ["name", "last_name", "birth_date", "adress"]
