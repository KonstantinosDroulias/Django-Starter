from django.db import models

# Create your models here.

class AppConfig(models.Model):
    app_name = models.CharField(max_length=255, default='Django Starter')
    app_tagline = models.CharField(max_length=255, default='My Awesome Project')
    app_author = models.CharField(max_length=255, default='Konstantinos Droulias')

    contact_email = models.EmailField(blank=True)

    maintenance_mode = models.BooleanField(default=False)
