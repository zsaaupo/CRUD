from rest_framework import serializers

from Student.models import StudentModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = [

            "full_name",
            "class_info",
            "section"
        ]
