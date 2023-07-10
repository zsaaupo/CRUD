from django.contrib import admin
from .models import *

class StudentModelAdmin(admin.ModelAdmin):
    fields = [

        "full_name",
        "class_info",
        "section"
    ]

    list_display = [

        "full_name",
        "class_info",
        "section"
    ]

admin.site.register(StudentModel, StudentModelAdmin)
