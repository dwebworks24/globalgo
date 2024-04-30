from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .healper import decrypt_user_id
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet
import pyotp 


@login_required
def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True, 'username': request.user.username})
    else:
        return JsonResponse({'authenticated': False})
    


def login_logic(request):
    if request.method == "POST":
        try:
            email = request.POST.get("emailId")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user:
                    if user.role.name == "admin":
                        print('admin')
                        return JsonResponse({'redirect_url': '/admin/'})
                    
                    elif user.role.name == "staff":
                        print("staff")
                        return JsonResponse({'redirect_url': '/staff_view/'})
                    else:
                        print("student")
                        return JsonResponse({'redirect_url': '/student_view/'})
            else:
                msg = 'Invalid credentials'
        
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
            return JsonResponse({'message': 'Method not allowed.'}, status=405)



@login_required
@csrf_exempt
def UserRegister(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get("username")
            phone = request.POST.get("phone")
            user_email = request.POST.get("emailId")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
           
            if password != confirm_password:
                return JsonResponse({'message': 'Passwords do not match.'}, status=400)

            if Users.objects.filter(username=user_name).exists():
                return JsonResponse({'message': 'Username already exists.'}, status=400)
            
            if Users.objects.filter(email=user_email).exists():
                return JsonResponse({'message': 'Email already exists.'}, status=400)
            roledata = Role.objects.all()
            new_user = Users()
            new_user.username=user_name
            new_user.email=user_email
            new_user.password=make_password(password)
            new_user.phone = phone
            new_user.profile_image = 'profile_images/default_profile.png'
            new_user.created_at = datetime.now()
            new_user.referal_code = request.user.referal_code
            new_user.is_active = True
            new_user.is_staff = True
            new_user.is_superuser = False
            new_user.role = roledata[2]
            new_user.save()
            save_User_data = Users.objects.filter(username=user_name,email=user_email,phone=phone)
            user_id = save_User_data[0].id
            
            return JsonResponse({'message': 'User registered successfully.','user_id':user_id})
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def staffRegister(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get("username")
            phone = request.POST.get("phone")
            user_email = request.POST.get("emailId")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
           
            if password != confirm_password:
                return JsonResponse({'message': 'Passwords do not match.'}, status=400)

            if Users.objects.filter(username=user_name).exists():
                return JsonResponse({'message': 'Username already exists.'}, status=400)
            
            if Users.objects.filter(email=user_email,).exists():
                return JsonResponse({'message': 'Email already exists.'}, status=400)
            roledata = Role.objects.all()
            new_user = Users()
            new_user.username=user_name
            new_user.email=user_email
            new_user.password=make_password(password)
            new_user.phone = phone
            new_user.profile_image = 'profile_images/default_profile.png'
            new_user.created_at = datetime.now()
            new_user.is_active = True
            new_user.is_staff = True
            new_user.is_superuser = False
            new_user.role = roledata[1]
            new_user.save()
        
            

            return JsonResponse({'message': 'Staff registered successfully.'})
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def updateprofile(request):
    if request.method == 'POST':
        try:
            userid = request.POST.get("userid")
            user_name = request.POST.get("username")
            phone = request.POST.get("phone")
            user_email = request.POST.get("emailId")
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            referal_code = request.POST.get("referal_code")
            dob = request.POST.get("dateofbirth")
            addres = request.POST.get("address")
            pincode = request.POST.get("pincode")
            profile_img = request.FILES.get("image")
           
          
            new_user =  Users.objects.filter(id=userid).first()
            new_user.username=user_name
            new_user.email=user_email
            new_user.phone = phone
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.date_of_birth = dob
            new_user.referal_code = referal_code
            new_user.pincode = pincode
            new_user.address = addres
            new_user.profile_image = profile_img
            new_user.save()

            return JsonResponse({'message': 'Profile updated successfully.'})
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)



@csrf_exempt
def verify_otp(request):
    try:
        post_data = request.POST
        enter_otp = post_data['enterOtp']
        otp_key = request.session.get('otp_secret_key')  # Fix typo here
        otp_valid_to = request.session.get('otp_valid_date')  # Fix typo here
        saved_otp = request.session.get('otp')  # Retrieve saved OTP from session
        if otp_key is not None and otp_valid_to is not None:
            valid_until = datetime.fromisoformat(otp_valid_to)
            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_key, interval=60)  # Corrected typo
                # if totp.verify(enter_otp):
                if enter_otp == saved_otp:
                    # OTP is verified, so delete the session data
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    del request.session['otp']
                    return JsonResponse({'message': 'OTP verified successfully.'})
                else:
                    return JsonResponse({'message': 'Entered OTP is invalid.'}, status=401)
            else:
                return JsonResponse({'message': 'OTP has expired.'}, status=401)
        else:
            return JsonResponse({'message': 'OTP verification data not found in session.'}), 
    except KeyError:
        return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    

@login_required
@csrf_exempt
def change_user_password(request):
    if request.method == 'POST':
        try:
            old_password = request.POST.get("oldPassword")
            new_password = request.POST.get("newPassword")
            confirm_password = request.POST.get("confirmPassword")

            user = request.user
            if user.check_password(old_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return JsonResponse({'message': 'Password updated successfully.'})
                else:
                    return JsonResponse({'message': 'New password and confirm password do not match.'}, status=400)
            else:
                
                return JsonResponse({'message': 'Incorrect old password.'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
        

@csrf_exempt
def password_reset(request):
    if request.method == 'POST':
        try:
            new_password = request.POST.get("newPassword")
            confirm_password = request.POST.get("confirmPassword")
            token_code = request.session.get('secret_token')
            token_key = request.session.get('secret_key')
            
            user_id = decrypt_user_id(token_code)
        
            user = Users.objects.filter(id=user_id).first()
            if user and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return JsonResponse({'message': 'Password updated successfully.'})
            else:
                return JsonResponse({'message': 'New password and confirm password do not match or user not found.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred: {}'.format(str(e))}, status=500)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)