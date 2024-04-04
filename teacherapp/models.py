from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class AdminHOD(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()



class Stream(models.Model):
    name = models.CharField(max_length=100)

class Class(models.Model):
    name = models.CharField(max_length=100)
    related_stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
class Teacher(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    related_stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()
class Timetable(models.Model):
    time_slot = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_name = models.OneToOneField(Class, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)  # Attendance tracking

    def __str__(self):
        return f"{self.time_slot} - {self.class_name} - {self.teacher}"


class Payment(models.Model):
     payment_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Payment rate per hour


class BasicSalary(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
class Bonus(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Deduction(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)



class NotificationTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    objects = models.Manager()

    def __str__(self):
        return f"{self.teacher} - {self.message}"


