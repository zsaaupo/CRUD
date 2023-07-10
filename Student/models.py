from django.contrib.auth.models import User
from django.db import models


class StudentModel(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100)
    class_info = models.PositiveIntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
        return self.full_name + " " + str(self.class_info) + " " + str(self.section)