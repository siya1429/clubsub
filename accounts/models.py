from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, sic, email, full_name, password=None):
        if not sic:
            raise ValueError("Users must have an sic number")

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            sic=sic,
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, sic, email, phone, full_name, password=None):
        user = self.create_user(
            sic=sic,
            email=email,
            password=password,
            phone=phone,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    sic = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name="email address", max_length=255)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "sic"
    REQUIRED_FIELDS = ["email", "full_name"]

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
