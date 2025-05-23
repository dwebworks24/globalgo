
from django.conf import settings
from django import template
from django.conf import settings
from django.template import loader
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from cryptography.fernet import Fernet
from .healper import send_otp_email_notification,send_smtp_mail,encrypt_user_id
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def visa_consultants_in_hyderabad(request):     
    return render(request, 'uifiles/visa-consultants-in-hyderabad.html')
def best_abroad_consultancy_in_telangana(request):     
    return render(request, 'uifiles/best_abroad_consultancy_in_telangana.html')
def best_consultancy_in_vijayawada(request):     
    return render(request, 'uifiles/best_consultancy_in_vijayawada.html')

def home(request):
    context ={}     
    context['Reviews'] = Reviews.objects.filter(is_approved = "approved")     
    return render(request, 'uifiles/home.html',context)
def best_abroad_consultancy_in_hyderabad(request):     
    return render(request, 'uifiles/best_abroad_consultancy_in_hyderabad.html')
def abroad_consultancy_in_andhra_pradesh(request):     
    return render(request, 'uifiles/abroad-consultancy-in-andhra-pradesh.html')
def abroad_consultancy_in_gannavaram(request):     
    return render(request, 'uifiles/abroad_consultancy_in_gannavaram.html')
def blogs(request):     
    return render(request, 'uifiles/blogs.html')
def home(request):     
    return render(request, 'uifiles/home.html')

def contactus(request):     
    return render(request, 'uifiles/contact.html')
def about(request):     
    return render(request, 'uifiles/about.html')
def services(request):     
    return render(request, 'uifiles/services.html')
def consultancy_in_vijayawada(request):     
    return render(request, 'uifiles/consultancy_in_vijayawada.html')
def visa_consultancy_services_in_vijayawada(request):     
    return render(request, 'uifiles/visa_consultancy_services_in_vijayawada.html')



def signin(request):
    context ={}
    try:
        return render(request, 'uifiles/login.html')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

def signup(request,countery_name,visatype):
    context ={}
    context['countryvisa'] = {'country_name': countery_name, 'visa_type': visatype}
    return render(request, 'uifiles/signup.html',context)

def admin_logout(request):
    x= 'text'
    logout(request)
    return redirect('/') 

@login_required
def staff_signup(request):
    context ={}
    try:
        return render(request, 'uifiles/staffregister.html')
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))


def otp_login(request):
    context ={}
    try:
        return render(request, 'uifiles/otp-view.html')
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required
def logout_view(request):
    try:
        logout(request)
        return redirect('/')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
      
@login_required
def adminView(request):
    context = {}
    staff_users = Users.objects.filter(role__name="staff")  
    context['users'] = staff_users 
    return render(request, 'uifiles/admin.html',context)

@login_required
def staff_details(request, user_id):
    context = {}
    try:
        context['user'] = Users.objects.filter(id=user_id).first()
        return render(request, 'uifiles/staff_details.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html',context)
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
def edit_staff_details(request, user_id):
    context = {}
    try:
        context['user'] = Users.objects.filter(id=user_id).first()
        return render(request, 'uifiles/edit_staff.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_staff_customers(request, staff_id):
    context = {}
    try:
        context['staff_customer'] = Users.objects.filter(id=staff_id)
        return render(request, 'uifiles/view_staf_customers.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_otp_verification(request):
    context = {}
    try:
        usenamename = request.user.username
        emailId = request.user.email
        send_otp_email_notification(request, name=usenamename, emailid=emailId)
        return render(request, 'uifiles/otp_verification.html',context)
     
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
def view_change_password(request):
    context = {}
    try:
        return render(request, 'uifiles/change_password.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))



def verify_email_resertpassword(request):
    context = {}
    try:
        return render(request, 'uifiles/resert_password.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@csrf_exempt    
def verify_email_link(request):
    context = {}
    try:
        post_data = request.POST
        get_email = post_data['email']
        get_user = Users.objects.filter(email=get_email) 
        if not get_user:
            return JsonResponse({'message': 'Your entered email is not found.'})
        if get_user is not None:
            userid = get_user[0].id
            encripted_token =  encrypt_user_id(userid)
            context['reset_password_link'] = f'{settings.SERVER_URL}/reset_user_password/{encripted_token}/'
            context['user'] = Users.objects.get(id=get_user[0].id)
        
        context['subject'] = f'Action Required: Password Reset for Your Account'
        
        load_template  =  'uifiles/email_template.html'
        html_template = loader.get_template( load_template )
        html_data = html_template.render(context)
        send_smtp_mail(SUBJECT=context['subject'],BODY='',HTML_DATA=html_data,RECIPIENT=[context['user'].email])
        return JsonResponse({'message': f'Mail sent successfully !!'})
    except Exception as e:
        return JsonResponse({'message': f'{e}'}, status=401)
    

@csrf_exempt    
def resert_change_password(request,token):
    context = {}
    try:
        request.session['secret_token'] = token
        return render(request, 'uifiles/resert_user_password.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
@csrf_exempt    
def student_view(request):
    context = {}
    try:
        country_list = Country.objects.all()
        context['country'] = country_list 
        return render(request, 'uifiles/student_view.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required
@csrf_exempt    
def customer_view(request):
    context = {'show_container': True }
    try:
        userid = request.user.id
        save_user = Users.objects.filter(id=userid).first()
        context['applicant'] = VisaApplication.objects.filter(user_id=userid).first()
        context['customer'] = save_user 
        application_number = context['applicant'].id
        country_list = Country.objects.all()
        context['country'] = country_list 
      
        return render(request, 'uifiles/customer_view.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
                            

@login_required
@csrf_exempt    
def countery_service_view(request,countery_name):
    context = {}
    try:
        visa_list = VisaTypes.objects.filter(Country__countery_name=countery_name)
        context['visa_type'] = visa_list 
        return render(request, 'uifiles/visa_service.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
@csrf_exempt        
def visa_application(request,userid):
    context = {}
    try:
        save_user = Users.objects.filter(id=userid).first()
        context['applicant'] = VisaApplication.objects.filter(user_id=userid).first()
        context['customer'] = save_user 
        application_number = context['applicant'].id
        context['uspoint'] = PointOfContact.objects.filter(application_user_id=application_number).first()
        context['cgi'] = SecurityQuestion.objects.filter(application_user_id=application_number).first()
        context['ceac'] = ceac_application.objects.filter(application_user_id=application_number).first()
        
        return render(request, 'uifiles/visa_application.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required
def update_profile_details(request, user_id):
    context = {}
    try:
        context['user'] = Users.objects.filter(id=user_id).first()
        return render(request, 'uifiles/update_profile.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
def visa_application_list(request,countery_name,visatype):
    context = {}
    try:
        context['countryvisa'] = {'country_name': countery_name, 'visa_type': visatype}
        context['application'] = VisaApplication.objects.filter(user__referal_code = request.user.referal_code,country=countery_name,visa_type=visatype).values(
            'id','applicationNo','user__first_name','user__last_name','user__email','user__phone','user__id'
        )
        # context['user'] = Users.objects.filter(referal_code =request.user.referal_code)
        return render(request, 'uifiles/application_list.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    

@login_required
def documents_list(request,applicationNo):
    context = {}
    try:
       
        context['application'] = VisaApplication.objects.filter(applicationNo=applicationNo).values(
            'id','applicationNo','upload_passport_front','upload_passport_back','aadhar_front','aadhar_back','user__id','doc_1', 'doc_2'
        ).first()
        user = context['application']['id']
        context['dependent'] = DependentDetails.objects.filter(application_user_id=user)
        return render(request, 'uifiles/documents_list.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
