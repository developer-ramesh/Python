from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question_text','pub_date']

admin.site.register(Question,QuestionAdmin)



from .models import Choice

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ['choice_text','question','votes']

admin.site.register(Choice,ChoiceAdmin)
