from django.db import models
import random

# Create your models here.
from django.contrib.auth.models import User


# Your custom models can be defined here
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    

    def generate_account_number(self, length=16):
        characters = "0123456789"
        
        
        while True:
            account_num = ''.join(random.choice(characters) for _ in range(length))
            if not Account.objects.filter(account_number=account_num).exists():
                self.account_number = account_num
                break  

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.generate_account_number()
        super(Account, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Account {self.account_number} - Balance: ${self.balance}"
    
class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        # Add additional user-related fields here if needed
        phone_number = models.CharField(max_length=15)
        address = models.CharField(max_length=100)

    # Other user-related fields...

        def __str__(self):
            return self.user.username