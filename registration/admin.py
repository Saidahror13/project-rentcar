from django.contrib import admin
from registration.models import User, AbstractUser

# Register your models here.
admin.site.register(User)
admin.site.register(AbstractUser)
