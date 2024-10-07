from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)

#how to change formate of admin file  structure
class SubjectMArksAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks']

admin.site.register(SubjectMarks ,SubjectMArksAdmin)
admin.site.register(Subject)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank' ,'total_marks', 'date_of_report_card_genration']
    ordering =  ['-student_rank']
    def total_marks(self, obj):
        subject_marks =  SubjectMarks.objects.filter(student = obj.student)
        marks =     (subject_marks.aggregate(marks = Sum('marks')))

        return marks["marks"]



admin.site.register(ReportCard , ReportCardAdmin)