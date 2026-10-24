
from django.shortcuts import render, redirect
from .forms import LoanApplicationForm
from .models import LoanApplication


# ==========================================
# HOME / LOGIN PAGE
# ==========================================

def login_page(request):
    return render(request, 'loan_app/login.html')


# ==========================================
# LOAN APPLICATION
# ==========================================

def loan_application(request):

    if request.method == 'POST':

        form = LoanApplicationForm(request.POST)

        if form.is_valid():

            loan = form.save(commit=False)

            loan.interest_rate = 10.0
            loan.loan_tenure = 12

            # Save first so EMI is calculated
            loan.save()

            loan_amount = float(loan.loan_amount)
            monthly_income = float(loan.monthly_income)
            emi = float(loan.emi)

            # Automatic loan decision
            if loan_amount > 1000000:

                loan.status = 'Pending'

            elif monthly_income >= emi * 3:

                loan.status = 'Approved'

            else:

                loan.status = 'Rejected'

            loan.save()

            # Store latest application ID
            request.session['application_id'] = loan.id

            return redirect('loan_success')

    else:

        form = LoanApplicationForm()

    return render(
        request,
        'loan_app/apply.html',
        {
            'form': form
        }
    )


# ==========================================
# SUCCESS PAGE
# ==========================================

def loan_success(request):

    application_id = request.session.get('application_id')

    if not application_id:

        return redirect('loan_application')

    try:

        application = LoanApplication.objects.get(
            id=application_id
        )

    except LoanApplication.DoesNotExist:

        request.session.pop(
            'application_id',
            None
        )

        return redirect('loan_application')

    return render(
        request,
        'loan_app/success.html',
        {
            'application': application
        }
    )


# ==========================================
# CHECK STATUS
# ==========================================

def check_status(request):

    application = None

    if request.method == 'POST':

        application_id = request.POST.get(
            'application_id'
        )

        try:

            application = LoanApplication.objects.get(
                id=application_id
            )

        except LoanApplication.DoesNotExist:

            application = None

    return render(
        request,
        'loan_app/status.html',
        {
            'application': application
        }
    )


# ==========================================
# LOAN DETAILS
# ==========================================

def loan_details(request):

    application = LoanApplication.objects.order_by(
        '-id'
    ).first()

    if application is None:

        return redirect('loan_application')

    return render(
        request,
        'loan_app/loan_details.html',
        {
            'application': application
        }
    )


# ==========================================
# EMPLOYEE LOGIN
# ==========================================


def employee_login(request):
    employee_username = os.environ.get("EMPLOYEE_USERNAME")
    employee_password = os.environ.get("EMPLOYEE_PASSWORD")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if (
            employee_username
            and employee_password
            and username == employee_username
            and password == employee_password
        ):
            request.session['employee_logged_in'] = True
            return redirect('employee_dashboard')

        return render(
            request,
            'loan_app/employee_login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'loan_app/employee_login.html')


# ==========================================
# EMPLOYEE LOGOUT
# ==========================================

def employee_logout(request):

    request.session.pop(
        'employee_logged_in',
        None
    )

    return redirect(
        'employee_login'
    )


# ==========================================
# EMPLOYEE DASHBOARD
# ==========================================

def employee_dashboard(request):

    if not request.session.get(
        'employee_logged_in'
    ):

        return redirect(
            'employee_login'
        )

    loans = LoanApplication.objects.all().order_by(
        '-created_at'
    )

    total_loans = LoanApplication.objects.count()

    pending_loans = LoanApplication.objects.filter(
        status='Pending'
    ).count()

    approved_loans = LoanApplication.objects.filter(
        status='Approved'
    ).count()

    rejected_loans = LoanApplication.objects.filter(
        status='Rejected'
    ).count()

    return render(
        request,
        'loan_app/dashboard.html',
        {
            'loans': loans,
            'total_loans': total_loans,
            'pending_loans': pending_loans,
            'approved_loans': approved_loans,
            'rejected_loans': rejected_loans,
        }
    )


# ==========================================
# APPROVE LOAN
# ==========================================

def approve_loan(request, loan_id):

    if not request.session.get(
        'employee_logged_in'
    ):

        return redirect(
            'employee_login'
        )

    try:

        loan = LoanApplication.objects.get(
            id=loan_id
        )

        loan.status = 'Approved'
        loan.save()

    except LoanApplication.DoesNotExist:

        pass

    return redirect(
        'employee_dashboard'
    )


# ==========================================
# REJECT LOAN
# ==========================================

def reject_loan(request, loan_id):

    if not request.session.get(
        'employee_logged_in'
    ):

        return redirect(
            'employee_login'
        )

    try:

        loan = LoanApplication.objects.get(
            id=loan_id
        )

        loan.status = 'Rejected'
        loan.save()

    except LoanApplication.DoesNotExist:

        pass

    return redirect(
        'employee_dashboard'
    )
# ==========================================
# APPLICATION STATUS
# ==========================================

def application_status(request):

    application = None

    if request.method == 'POST':

        application_id = request.POST.get('application_id')

        try:
            application = LoanApplication.objects.get(
                id=application_id
            )
        except LoanApplication.DoesNotExist:
            application = None

    return render(
        request,
        'loan_app/application_status.html',
        {
            'application': application
        }
    )