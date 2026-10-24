from django.contrib import admin
from .models import LoanApplication


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'loan_amount',
        'loan_type',
        'status',
        'created_at',
    )

    list_filter = ('status', 'loan_type', 'created_at')

    search_fields = ('name', 'email', 'phone')

    ordering = ('-created_at',)