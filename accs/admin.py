from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import *


class QuizResource(resources.ModelResource):

    class Meta:
        model = Quiz
        fields = (
            "name",
            "uname",
            "res",
            "questions",
            "date_created",
        )


class QuizAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = QuizResource


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
