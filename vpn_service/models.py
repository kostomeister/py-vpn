from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)


class Site(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class SiteStatistics(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="statistics")
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="statistics")
    data_size = models.BigIntegerField(default=0)
    page_transitions_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.site.name}"
