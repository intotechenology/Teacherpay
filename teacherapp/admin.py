from django.contrib import admin
from .models import Profile, AdminHOD, Teacher, Stream, Class, Timetable, Payment, Bonus, Deduction, NotificationTeacher,BasicSalary

# admin.py


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_admin', 'is_staff']

@admin.register(AdminHOD)
class AdminHODAdmin(admin.ModelAdmin):
    list_display = ['admin', 'department', 'created_at', 'updated_at']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['admin', 'address', 'created_at', 'updated_at']

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'related_stream']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['time_slot', 'start_time', 'end_time', 'class_name', 'teacher', 'attended']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_rate',]

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'amount']

@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'amount']

@admin.register(NotificationTeacher)
class NotificationTeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'message', 'created_at', 'updated_at']



@admin.register(BasicSalary)
class BasicSalaryAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'amount', ]

