from django import forms
from .models import LoanApplication


class LoanApplicationForm(forms.ModelForm):

    loan_type = forms.ChoiceField(
        choices=[
            ('', 'Select Loan Type'),
            ('Personal Loan', 'Personal Loan'),
            ('Home Loan', 'Home Loan'),
            ('Education Loan', 'Education Loan'),
            ('Vehicle Loan', 'Vehicle Loan'),
            ('Business Loan', 'Business Loan'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    employment = forms.ChoiceField(
        choices=[
            ('', 'Select Employment Type'),
            ('Salaried', 'Salaried'),
            ('Self Employed', 'Self Employed'),
            ('Business Owner', 'Business Owner'),
            ('Student', 'Student'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = LoanApplication

        fields = [
            'name',
            'email',
            'phone',
            'loan_type',
            'loan_amount',
            'monthly_income',
            'employment',
            'purpose',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 10-digit phone number'
            }),

            'loan_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter loan amount',
                'min': '1'
            }),

            'monthly_income': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter monthly income',
                'min': '1'
            }),

            'purpose': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us why you need this loan',
                'rows': 4
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only letters."
            )

        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number should contain only digits."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone

    def clean_monthly_income(self):
        income = self.cleaned_data.get('monthly_income')

        if income is not None and income <= 0:
            raise forms.ValidationError(
                "Monthly income must be greater than 0."
            )

        return income

    def clean_loan_amount(self):
        amount = self.cleaned_data.get('loan_amount')

        if amount is not None and amount <= 0:
            raise forms.ValidationError(
                "Loan amount must be greater than 0."
            )

        return amount