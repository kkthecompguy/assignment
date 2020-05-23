from django import forms
from .models import Student, Residence, Contact, Medical, School, Game

class StudentForm(forms.ModelForm):
  dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  entry_year = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  year_attended = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
  class Meta:
    model = Student
    fields = '__all__'


class ResidenceForm(forms.ModelForm):
  street_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  street_address_line_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  home_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  cell_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_street_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_street_address_line_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_home_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  p_cell_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_street_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_street_address_line_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_home_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  g_cell_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Residence
    fields = '__all__'


class ContactForm(forms.ModelForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  first_name_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  phone_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  class Meta:
    model = Contact
    fields = '__all__'
    exclude =  ['student_id']


class MedicalForm(forms.ModelForm):
  doc_first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  doc_last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  hospital = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  insurance_cover = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  health_info = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  class Meta:
    model = Medical
    fields = '__all__'


class SchoolForm(forms.ModelForm):
  school_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
  end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
  school_name_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  city_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  state_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  start_date_2 = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
  end_date_2 = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

  class Meta:
    model = School
    fields = '__all__'


class GameForm(forms.ModelForm):
  game = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  level = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Game
    fields = '__all__'