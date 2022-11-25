from django.urls import path

from employees import views

app_name = "employees"
urlpatterns = [
    path("employees", views.StudentListView.as_view(), name="employees-list"),
    path("employees/add/", views.StudentCreateView.as_view(), name="employees-add"),
    path("employees/<int:pk>/detail/", views.EmployeesDetailView.as_view(), name="employees-detail"),
    path("employees/<int:pk>/update/", views.EmployeesUpdateView.as_view(), name="employees-update"),
    path("employees/<int:pk>/delete/", views.EmployeesDeleteView.as_view(), name="employees-delete"),
]