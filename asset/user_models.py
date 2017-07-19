from django.db import models

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,password=password,name=name)
        user.is_admin=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email=models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length= 32)
    is_active = models.BooleanField(default= True)
    is_admin=models.BooleanField(default=False)

    objects=UserProfileManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin