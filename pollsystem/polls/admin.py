from django.contrib import admin

# Register your models here.

from .models import Question, Choice



# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "Admin YourPoll"
admin.site.site_title = "YourPoll Admin Area"
admin.site.index_title = "Welcome to the YourPoll Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['p_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
