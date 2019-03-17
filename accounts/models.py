from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser , BaseUserManager
)
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, fullname, phone, password=None, is_active=True, is_staff=False, is_admin=False):
        if not phone:
            raise ValueError("User Must have valid phone no")
        if not fullname:
            raise ValueError("Enter full name")
        if not password:
            raise ValueError("User must have a job")

        user_obj = self.model(
            phone =self.normalize_email(phone),
            fullname = fullname,
            #job_post=job_post
        )
        user_obj.set_password(password)
        user_obj.active=is_active
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self, fullname, phone, password):
        #password = 'job_post'
        user =self.create_user(
                phone,
                fullname,
            #    job_post,
                password=password,
                is_staff=True
        )
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self, fullname,  phone, password):
        #password = 'job_post'
        user =self.create_user(
                phone,
                fullname,
            #    job_post,
                password=password,
                is_admin=True
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    job_post = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
    )
    fullname  = models.CharField(max_length=200, default='')
    job_post  = models.CharField(max_length= 30, choices = job_post)
    phone = models.CharField(max_length=10, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    #timestamp =models.DateTimeField(blank=True, default= '')

    ##Custom user name and password
    USERNAME_FIELD = 'phone'
    PASSWORD_FIELD = 'job_post'
    #username and password are required field bydefaults
    REQUIRED_FIELDS= ['fullname',]

    objects =UserManager()

    def _str_(self):
        return self.phone
    def get_full_name(self):
        return self.phone
    def get_short_name(self):
        return self.phone
    def has_perm(self,perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.DO_NOTHING)


class GuestEmail(models.Model):
    job_post = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
    )
    name  = models.CharField(max_length=200, default='')
    fullname=models.CharField(max_length=200,default='')
    job_post  = models.CharField(max_length= 30, choices = job_post)
    phone = models.CharField(max_length=10 , default='')
    opid    = models.CharField(max_length=20, default='')

    def _str_ (self):
       return self.phone
