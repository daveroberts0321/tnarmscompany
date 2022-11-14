from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Customer(models.Model):
	user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)
