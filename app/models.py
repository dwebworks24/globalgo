from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations =True
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not phone:
            raise ValueError("Phone number is required")

        # Normalize email address
        email = self.normalize_email(email)

        # Create and save the user with required fields
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        # Create a superuser with required fields and additional permissions
        user = self.create_user(email, username, phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
# class Role(models.Model):
#     name = models.CharField(max_length=255,default='admin',unique=True)

#     def __str__(self):
#         return self.name

user_roles = (
        ('admin', 'admin'),
        ('staff', 'staff'),
        ('customer','customer'),
    )

    
class Users(AbstractBaseUser, PermissionsMixin):
    # Custom user model fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    referal_code  = models.CharField(max_length=100,blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Required for custom user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define the field to be used as the unique identifier for logging in
    USERNAME_FIELD = 'email'
    # Additional fields required when creating a user
    REQUIRED_FIELDS = ['username', 'phone']

    # Custom user manager
    objects = UserManager()

    role = models.CharField(choices=user_roles,max_length=100,null=True,blank=True,default='admin')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
         return True


class Country(models.Model):
    countery_name = models.CharField(max_length=100, blank=True, null=True)
    country_logo = models.ImageField(upload_to='country_images/', blank=True, null=True)
    image = models.ImageField(upload_to='country_images/', blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user_id')
    created_by = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,related_name='created_country',db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'country_list'


Visa_Types = (
        ('visit', 'visit'),
        ('Tourist', 'Tourist'),
        ('Study', 'Study'),
        ('Medical', 'Medical'),
        ('Migration', 'Migration'),
        ('Family', 'Family'),
        ('Diplomatic', 'Diplomatic'),
        ('Working', 'Working'),
        ('Business', 'Business'),

    )
class VisaTypes(models.Model):
    Country = models.ForeignKey('Country', models.DO_NOTHING, null=False,blank=False,db_column='Country_id')
    country_logo = models.ImageField(upload_to='country_images/', blank=True, null=True)
    Visa_Types = models.CharField(choices=Visa_Types,max_length=100,null=True,blank=True,default='visit visa')
    Description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,related_name='created_country_type',db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'visa_types_list'
    def __str__(self):
        return self.Country.countery_name


class DependentDetails(models.Model):
    dependent_first_name = models.CharField(max_length=100, blank=True, null=True)
    dependent_last_name = models.CharField(max_length=100, blank=True, null=True)
    dependent_email = models.EmailField()
    dependent_phone = models.CharField(max_length=13, blank=True, null=True)
    dependent_phone_number_two = models.CharField(max_length=13, blank=True, null=True)
    upload_passport_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    upload_passport_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    aadhar_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    aadhar_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    # user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user-dependent_id')
    application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='VisaApplication_id')
    class Meta:
        managed = True
        db_table = 'dependent_list'

class PointOfContact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    relation_ship = models.CharField(max_length=255,blank=True, null=True)
    organization_name = models.CharField(max_length=255,blank=True, null=True)
    professional_experience = models.CharField(max_length=255,blank=True, null=True)
    organization_address = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True, null=True)
    street_name= models.CharField(max_length=255,blank=True, null=True)
    street_name_address = models.CharField(max_length=255,blank=True, null=True)
    city =  models.CharField(max_length=100,blank=True, null=True)
    state =  models.CharField(max_length=100,blank=True, null=True)
    zipcode =  models.CharField(max_length=100,blank=True, null=True)
    # user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='point_of_contact_user_id')
    application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='visaApplication_id')
    class Meta:
        managed = True
        db_table = 'point_of_contact'

class SecurityQuestion(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    questio1 = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    questio2 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    questio3 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='visaApplication_id')
    
    class Meta:
        managed = True
        db_table = 'security_question'


class ceac_application(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    questio = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='visaApplication_id')
    
    class Meta:
        managed = True
        db_table = 'ceac_application'

class VisaApplication(models.Model):
    applicationNo = models.IntegerField()
    phone_number_two = models.CharField(max_length=13, blank=True, null=True)
    upload_passport_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    upload_passport_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    aadhar_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    aadhar_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
    country = models.CharField(max_length=13, blank=True, null=True, default='')
    visa_type = models.CharField(max_length=13, blank=True, null=True, default='')
    phone_number_two = models.CharField(max_length=13, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user_visa_application_id')

    class Meta:
        managed = True
        db_table = 'visa_application'
 


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'contact'
 