from django.db import models
from decimal import Decimal


class LoanApplication(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_type = models.CharField(max_length=50)

    monthly_income = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    employment = models.CharField(max_length=100)
    purpose = models.TextField()

    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10.0
    )

    loan_tenure = models.PositiveIntegerField(
        default=12
    )

    emi = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_emi(self):
        principal = Decimal(self.loan_amount)
        annual_rate = Decimal(self.interest_rate)
        months = Decimal(self.loan_tenure)

        if principal <= 0 or months <= 0:
            return Decimal('0.00')

        monthly_rate = annual_rate / Decimal('1200')

        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = (
                principal
                * monthly_rate
                * (1 + monthly_rate) ** months
                / ((1 + monthly_rate) ** months - 1)
            )

        return round(emi, 2)

    def save(self, *args, **kwargs):
        self.emi = self.calculate_emi()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name