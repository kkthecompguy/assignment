from django.contrib import admin
from .models import Student, Contact, Residence, School, Medical, Game

# Register your models here.
admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Residence)
admin.site.register(School)
admin.site.register(Medical)
admin.site.register(Game)
