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
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


    
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

    role = models.ForeignKey('Role', models.DO_NOTHING, default=None, null=False,blank=False,db_column='role_id')

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
        ('visit visa', 'visit visa'),
        ('Tourist Visa', 'Tourist Visa'),
        ('Study Visa', 'Study Visa'),
        ('Medical Visa', 'Medical Visa'),
        ('Migration Visa', 'Migration Visa'),
        ('Family Visa', 'Family Visa'),
        ('Diplomatic Visa', 'Diplomatic Visa'),
        ('Working Visa', 'Working Visa'),
        ('Business Visa', 'Business Visa'),

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


# class DependentDetails(models.Model):
#     Dependent_first_name = models.CharField(max_length=100, blank=True, null=True)
#     Dependent_last_name = models.CharField(max_length=100, blank=True, null=True)
#     Dependent_email = models.EmailField()
#     dDependent_phone = models.CharField(max_length=20, blank=True, null=True)
#     Dependent_PhoneNumber_two = models.CharField(max_length=13, blank=True, null=True)
#     UploadPassport_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     UploadPassport_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     Aadhar_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     Aadhar_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user-dependent_id')
#     application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='VisaApplication_id')
#     class Meta:
#         managed = True
#         db_table = 'dependent_list'

# class PointOfContact(models.Model):
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20,blank=True, null=True)
#     address_line1 = models.CharField(max_length=255,blank=True, null=True)
#     address_line2 = models.CharField(max_length=255,blank=True, null=True)
#     city =  models.CharField(max_length=100,blank=True, null=True)
#     state =  models.CharField(max_length=100,blank=True, null=True)
#     zipcode =  models.CharField(max_length=100,blank=True, null=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='point_of_contact_user_id')
#     application_user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='visaApplication_id')
#     class Meta:
#         managed = True
#         db_table = 'poin_of_contact'

# class SecurityQuestion(models.Model):
#     username = models.CharField(max_length=100, blank=True, null=True)
#     password = models.CharField(max_length=100, blank=True, null=True)
#     questio1 = models.CharField(max_length=255)
#     answer1 = models.CharField(max_length=255)
#     questio2 = models.CharField(max_length=255)
#     answer2 = models.CharField(max_length=255)
#     questio3 = models.CharField(max_length=255)
#     answer3 = models.CharField(max_length=255)
#     user = models.ForeignKey('VisaApplication', models.DO_NOTHING, null=False,blank=False,db_column='visaApplication_id')
    
#     class Meta:
#         managed = True
#         db_table = 'security_question'


# class VisaApplication(models.Model):
#     ApplicationNo = models.IntegerField()
#     PhoneNumber_two = models.CharField(max_length=13, blank=True, null=True)
#     UploadPassport_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     UploadPassport_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     Aadhar_front = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     Aadhar_back = models.ImageField(upload_to='visaapplication/', blank=True, null=True)
#     PointOfContact_email = models.EmailField()
#     PointOfContact_phone = models.CharField(blank=True, null=True,max_length=20)
#     PointOfContact_address = models.TextField(blank=True, null=True,max_length=255)
    
    


#     image = models.ImageField(upload_to='country_images/', blank=True, null=True)
#     countery_name = models.CharField(max_length=100, blank=True, null=True)
#     country_logo = models.ImageField(upload_to='country_images/', blank=True, null=True)
#     image = models.ImageField(upload_to='country_images/', blank=True, null=True)
#     Description = models.TextField(blank=True, null=True)
#     user = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,db_column='user_id')
#     created_by = models.ForeignKey('Users', models.DO_NOTHING, null=False,blank=False,related_name='created_country',db_column='created_by')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         managed = True
#         db_table = 'country_list'