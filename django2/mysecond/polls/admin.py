from django.contrib import admin
from .models import Question, Choice


# StackedInline 상속
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('일자', {'fields': ['pub_date'], 'classes': ['collapse']})]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
