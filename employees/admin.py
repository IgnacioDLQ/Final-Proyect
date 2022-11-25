from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    name = models.CharField(max_length=40)
    birth_date = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adress = models.CharField(max_length=40)
    list_display = ("name", "birth_date", "last_name", "adress")
    
    def __str__(self):
        return f"{self.name} {self.last_name} | info : {self.birth_date} {self.adress}"
