from django.db import models
from django.shortcuts import redirect, reverse

GENDER = (
  ('Male', 'Male'),
  ('Female', 'Female'),
)

SEMESTER = (
  ('1', '1'),
  ('2', '2'),
)

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  dob = models.DateField()
  gender = models.CharField(max_length=10, choices=GENDER)
  ethnicity = models.CharField(max_length=20)
  email = models.EmailField()
  entry_year = models.DateField()
  grade = models.CharField(max_length=1)
  previously_attended = models.BooleanField()
  year_attended = models.DateField(null=True, blank=True)
  semester = models.CharField(max_length=1, choices=SEMESTER)

  def __str__(self):
    return self.first_name

  def get_absolute_url(self):
    return redirect('student-detail', pk=self.pk)


class Residence(models.Model):
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  street_address = models.CharField(max_length=20)
  street_address_line_2 = models.CharField(max_length=20)
  city = models.CharField(max_length=10)
  state = models.CharField(max_length=10)
  zip_code = models.CharField(max_length=5)
  home_phone = models.CharField(max_length=13)
  cell_phone = models.CharField(max_length=13)
  p_street_address = models.CharField(max_length=20, blank=True, null=True)
  p_street_address_line_2 = models.CharField(max_length=50, blank=True, null=True)
  p_city = models.CharField(max_length=10, blank=True, null=True)
  p_state = models.CharField(max_length=10, blank=True, null=True)
  p_zip_code = models.CharField(max_length=5, blank=True, null=True)
  p_home_phone = models.CharField(max_length=13, blank=True, null=True)
  p_cell_phone = models.CharField(max_length=13, blank=True, null=True)
  g_street_address = models.CharField(max_length=20, blank=True, null=True)
  g_street_address_line_2 = models.CharField(max_length=50, blank=True, null=True)
  g_city = models.CharField(max_length=10, blank=True, null=True)
  g_state = models.CharField(max_length=10, blank=True, null=True)
  g_zip_code = models.CharField(max_length=5, blank=True, null=True)
  g_home_phone = models.CharField(max_length=13, blank=True, null=True)
  g_cell_phone = models.CharField(max_length=13, blank=True, null=True)
  
  def __str__(self):
    return self.street_address


class Contact(models.Model):
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=13)
  first_name_2 = models.CharField(max_length=100)
  last_name_2 = models.CharField(max_length=100)
  phone_2 = models.CharField(max_length=13)

  def __str__(self):
    return self.first_name


class Medical(models.Model):
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  doc_first_name = models.CharField(max_length=50)
  doc_last_name = models.CharField(max_length=50)
  hospital = models.CharField(max_length=50)
  insurance_cover = models.CharField(max_length=50)
  health_info = models.TextField()

  def __str__(self):
    return self.doc_first_name


class School(models.Model):
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  school_name = models.CharField(max_length=50)
  city = models.CharField(max_length=10)
  state = models.CharField(max_length=10)
  start_date = models.DateField()
  end_date = models.DateField()
  school_name_2 = models.CharField(max_length=50, blank=True, null=True)
  city_2 = models.CharField(max_length=10, blank=True, null=True)
  state_2 = models.CharField(max_length=10, blank=True, null=True)
  start_date_2 = models.DateField(blank=True, null=True)
  end_date_2 = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.school_name


class Game(models.Model):
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  game = models.CharField(max_length=20)
  level = models.CharField(max_length=20)

  def __str__(self):
    return self.student_id.first_name
