from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, logout,login
from django.contrib import auth, messages
from .forms  import LoginForm,CreateUserForm,SalaryForm
from django.contrib.auth.decorators import login_required
from .models import models,Timetable, Payment, BasicSalary, Deduction, Bonus,Teacher
from decimal import Decimal
# Create your views here.



def logoutView(request):
	logout(request)
	return redirect('home')

def login_user(request):
    if request.method == 'POST':
          username=request.POST.get('username')
          password=request.POST.get('password')

          user=authenticate(request,username=username,password=password)
          if user is not None:
                  login(request,user)
                  profile = user.profile
                  if profile.is_admin:
                      return redirect('admindash')
                  
                  else:
                    return redirect('staff')
                  
          else:
               messages.info(request,'Username OR Password is Incorrect')
               return render(request,'appauth/login.html',context)
    context={}
    return render(request,'appauth/login.html',context )

def user_register(request):
    if request.user.is_authenticated:
         return redirect('teacher')
    else:
          form=CreateUserForm()
    if request.method=="POST":
      form=CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request,"Account created succesfully for " +user)
        return redirect('home')
    

    context={'form':form}

    return render(request,'appauth/register.html',context )


@login_required(login_url="login")
def teacherdash(request):
     return render(request,'teacher/teacher.html')




def admin_dash(request):
     

     
     return render(request, 'staff/admindash.html')


def admin_teacher_salary_view(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            # Process form data
            # Example: Save form data to database
            for teacher in teachers:
                # Get the bonus and deduction values for the current teacher
                bonus_key = f"bonus_{teacher.id}"
                deduction_key = f"deduction_{teacher.id}"
                bonus = form.cleaned_data.get(bonus_key)
                deduction = form.cleaned_data.get(deduction_key)
                # Save or update the teacher's salary information
                teacher.basic_salary = form.cleaned_data['basic_salary']
                teacher.payment_rate = form.cleaned_data['payment_rate']
                teacher.save()
            return redirect('userview')  # Redirect to success page
    else:
        form = SalaryForm()

    context = {
        'teachers': teachers,
        'form': form,
    }
    return render(request, 'staff/salaryform.html', context)
 
def staff(request):
     return render(request,'staff/staff.html')
def adminView(request):
     return render(request, "staff/adviewuser.html")
def detail(request):
     return render(request, 'staff/add.html')





# views.py



def calculate_salary(teacher):
    # Retrieve payment rate per hour
    payment_rate = Payment.objects.first().payment_rate  # Assuming there's only one payment rate
    
    # Calculate total hours worked by the teacher
    hours_worked = Timetable.objects.filter(teacher=teacher, attended=True).count()
    
    # Retrieve basic salary for the teacher
    try:
        basic_salary = BasicSalary.objects.get(teacher=teacher).amount
    except BasicSalary.DoesNotExist:
        basic_salary = Decimal('0.00')  # If basic salary is not set, default to 0
    
    # Calculate total salary based on hours worked and payment rate
    total_salary = hours_worked * payment_rate
    
    # Retrieve total deductions for the teacher
    total_deductions = Deduction.objects.filter(teacher=teacher).aggregate(total_deductions=models.Sum('amount'))['total_deductions']
    if not total_deductions:
        total_deductions = Decimal('0.00')
    
    # Retrieve total bonuses for the teacher
    total_bonuses = Bonus.objects.filter(teacher=teacher).aggregate(total_bonuses=models.Sum('amount'))['total_bonuses']
    if not total_bonuses:
        total_bonuses = Decimal('0.00')
    
    # Calculate final salary after adding bonuses and deducting deductions
    final_salary = total_salary + basic_salary + total_bonuses - total_deductions
    
    return final_salary

def teacher_dashboard(request):
    teacher = request.user  # Assuming you have a User model associated with the teacher
    salary = calculate_salary(teacher)
    return render(request, 'teacher_dashboard.html', {'salary': salary})
