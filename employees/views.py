from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from employees.models import Employee
from employees.forms import EmployeeForm


class EmployeeListView(ListView):
    model = Employee
    paginate_by = 3


class EmployeeDetailView(DetailView):
    model = Employee
    fields = ["name", "last_name", "email", "profession"]


class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    success_url = reverse_lazy("profesor:profesor-list")

    form_class = EmployeeForm

    def form_valid(self, form):
        """Filter to avoid duplicated employees"""
        data = form.cleaned_data
        actual_objects = Employee.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            adress=data["adress"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El empleado {data['name']} {data['last_name']} | {data['birth_date']} | {data['adress']} ya existe",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El empleado: {data['name']} - {data['last_name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ["name", "last_name", "birth_date", "adress"]

    def get_success_url(self):
        employee_id = self.kwargs["pk"]
        return reverse_lazy("employee:employee-detail", kwargs={"pk": employee_id})


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:employee-list")

