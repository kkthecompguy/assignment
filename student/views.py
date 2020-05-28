from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student, Medical
from .forms import StudentForm, ResidenceForm, ContactForm, MedicalForm, SchoolForm, GameForm

# Create your views here.
def index(request):
  form = StudentForm()
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('student-list')
  context = {
    'form': form
  }
  return render(request, 'student/student-info.html', context)


def residence(request, pk):
  student = get_object_or_404(Student, pk=pk)
  form = ResidenceForm()
  if request.method == 'POST':
    form = ResidenceForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('contact', pk=pk)
  context = {
    'form': form,
    'student': student
  }
  return render(request, 'student/residence.html', context)


def contact(request, pk):
  student = get_object_or_404(Student, pk=pk)
  form = ContactForm()
  if request.method == 'POST':
    print(request.POST)
    form = ContactForm(request.POST)
    print(form)
    if form.is_valid():
      print(True)
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('medical', pk=pk)
  context = {
    'form': form,
    'student': student
  }
  return render(request, 'student/contact.html', context)


def medical(request, pk):
  student = get_object_or_404(Student, pk=pk)
  
  form = MedicalForm()
  if request.method == 'POST':
    # print(request.POST)
    form = MedicalForm(request.POST)
    print(form)
    if form.is_valid():
      print(True)
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('school', pk=pk)
  context = {
    'form': form,
    'student': student
  }
  return render(request, 'student/medical.html', context)


def school(request, pk):
  student = get_object_or_404(Student, pk=pk)
  form = SchoolForm()
  if request.method == 'POST':
    form = SchoolForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('game', pk=pk)
  context = {
    'form': form,
    'student': student
  }
  return render(request, 'student/school.html', context)


def game(request, pk):
  student = get_object_or_404(Student, pk=pk)
  form = GameForm()
  if request.method == 'POST':
    form = GameForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Your details were saved successfully")
      return redirect('student-detail', pk=pk)
  context = {
    'form': form,
    'student': student
  }
  return render(request, 'student/game.html', context)


def student_list_view(request):
  students = Student.objects.all()
  context = {
    'students': students
  }
  return render(request, 'student/student-list.html', context)


def student_detail(request, pk):
  student = get_object_or_404(Student, pk=pk)
  residence_info = student.residence_set.all().count() 
  contact_info = student.contact_set.all().count()
  medical_info = student.medical_set.all().count()
  school_info = student.school_set.all().count()
  game_info = student.game_set.all().count()
  context = {
    'student': student,
    'residence_info': residence_info,
    'contact_info': contact_info,
    'medical_info':  medical_info,
    'school_info': school_info,
    'game_info': game_info
  }
  return render(request, 'student/student-detail.html', context)