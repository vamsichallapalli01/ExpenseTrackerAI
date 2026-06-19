from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    source = models.CharField(
        max_length=100
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    def __str__(self):
        return self.source


class Expense(models.Model):

    CATEGORY_CHOICES = [

        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Gas', 'Gas'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Travel', 'Travel'),
        ('Healthcare', 'Healthcare'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    description = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.category

class Budget(models.Model):

    CURRENCY_CHOICES = [

        ('USD', '$ US Dollar'),
        ('INR', '₹ Indian Rupee'),
        ('EUR', '€ Euro'),
        ('GBP', '£ British Pound'),

    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    monthly_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default='USD'
    )

    def __str__(self):
        return str(self.monthly_budget)  
     
class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):

        return self.user.username 
    
class RecurringExpense(models.Model):

    FREQUENCY_CHOICES = [

        ('Monthly', 'Monthly'),

        ('Weekly', 'Weekly')

    ]

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )

    name = models.CharField(

        max_length=100

    )

    amount = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )

    frequency = models.CharField(

        max_length=20,

        choices=FREQUENCY_CHOICES

    )

    def __str__(self):

        return self.name
    

class Receipt(models.Model):

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )

    image = models.ImageField(

        upload_to='receipts/'

    )

    uploaded_at = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):

        return str(self.id)