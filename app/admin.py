import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import *
# Register your models here.
class AdminUserlist(admin.ModelAdmin):
    list_display=('id','username','password','email')
    list_filter = ['username','email','phone','referal_code']
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"



class AdminCountry(admin.ModelAdmin):
    list_display=('id','countery_name')

class AdminCountryTpes(admin.ModelAdmin):
    list_display=('id','Country','Visa_Types','Description')

class AdminDependentDetails(admin.ModelAdmin):
    list_display=('id','dependent_first_name','dependent_last_name','dependent_email','dependent_phone')


class AdminPointOfContact(admin.ModelAdmin):
    list_display=('id','first_name','email','phone','city','state','zipcode')


class AdminSecurityQuestion(admin.ModelAdmin):
    list_display=('id','username','password','questio1','answer1','questio2','answer2','questio3','answer3')

class AdminVisaApplication(admin.ModelAdmin):
    list_display=('applicationNo','phone_number_two','user_id')

class AdminContact(admin.ModelAdmin):
    list_display=('id','first_name' ,'email','phone','subject','message')                  

admin.site.register(Users,AdminUserlist)
admin.site.register(Country,AdminCountry)
admin.site.register(VisaTypes,AdminCountryTpes)
admin.site.register(DependentDetails,AdminDependentDetails)
admin.site.register(PointOfContact,AdminPointOfContact)
admin.site.register(SecurityQuestion,AdminSecurityQuestion)
admin.site.register(VisaApplication,AdminVisaApplication)
admin.site.register(Contact,AdminContact)
