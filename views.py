# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from courses.models import Course, Enrollment

def index(request):
    courses = Course.objects.filter(is_published=True)[:6]
    return render(request, 'index.html', {'courses': courses})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {
        'enrollments': enrollments
    })
