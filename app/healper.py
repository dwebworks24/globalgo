from django.conf import settings
from django.http.response import JsonResponse
from django.core.mail import send_mail
from datetime import datetime,timedelta
from django.core.mail import EmailMultiAlternatives
from cryptography.fernet import Fernet
from typing import List
import pyotp 
import json
from .models import *
from django.core import signing
from django.db.models import Max


def encrypt_user_id(user_id):
    encrypted_data  = signing.dumps(user_id)
    print(encrypted_data)
    return encrypted_data 

def decrypt_user_id(encrypted_user_id):
    decrypted_data = signing.loads(encrypted_user_id)
    return decrypted_data
   



def generate_email_message(otp,name):
    body = f"Hello {name},\n\nYour OTP for login: {otp}.\n\nPlease use this OTP to proceed to login.\n\nIf you didn't request this change, please ignore this email.\n\nBest regards,\nGlobalGo"
    return body

def send_otp_email(subject,body,sender_email, receipt_email):

    try:
        send_mail(subject, body, sender_email, [receipt_email])
        print("OTP email sent successfully.")
    except Exception as e:
        print("Error sending OTP email:", str(e))
    

#generate email notification and opt generation
def send_otp_email_notification(request,name,emailid):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()
    sender_emailid = settings.EMAIL_HOST_USER
    subject = 'Password Change OTP'
    body = generate_email_message(otp,name)
    print('your OTP:',otp)
    send_otp_email(subject,body,sender_email=sender_emailid,receipt_email=emailid)
    return otp 

class Attachments:
    filename: str = None
    file: str = None
    mime_type: str = None
    
    def __init__(self,filename=None,file=None,mime_type='application/pdf'):
        self.filename = str(filename).replace(".","_")
        self.file = file
        self.mime_type = mime_type
        
def send_smtp_mail(SUBJECT,BODY,HTML_DATA=None,RECIPIENT=[],CC_EMAILS=[],attachments: List[Attachments] = []):
    try:
        email = EmailMultiAlternatives(subject=SUBJECT,body=BODY,to=RECIPIENT,cc=CC_EMAILS)
        email.attach_alternative(content=HTML_DATA,mimetype='text/html')
        for attach in attachments:
            email.attach(filename=attach.filename,content=attach.file,mimetype=attach.mime_type)
        email.send()
    except Exception as e:
        pass



def generate_visa_application():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    g_string = f"{year}{month:02d}{day:02d}"
    return g_string
