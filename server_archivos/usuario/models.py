from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserManagerCustom(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Debe de ingresar el email para continuar")

        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        if password:
            user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email,
        password=None,
        **extra_fields,
    ):
        if not email:
            raise ValueError("Debe de ingresar el email para continuar")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        if password:
            user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Correo electronico",
    )

    # Proceso para poder loguearse con el email y no con el username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    # Usa custom manager para prevenir error:
    # TypeError: UserManager.create_superuser() missing 1 required positional argument: 'username'
    objects = UserManagerCustom()

    class Meta:
        db_table = "usuario"
        managed = True
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["id"]

    def __str__(self):
        return f"{self.username} - {self.email}"

    def deactivate(self):
        self.is_active = False
        self.save()

    def reactivate(self):
        self.is_active = True
        self.save()
