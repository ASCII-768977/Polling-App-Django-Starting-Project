from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "Polling System"
admin.site.index_title = "This is a polling system"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)