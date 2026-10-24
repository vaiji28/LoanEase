from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.login_page,
        name="home"
    ),

    path(
        "employee-login/",
        views.employee_login,
        name="employee_login"
    ),

    path(
        "employee-logout/",
        views.employee_logout,
        name="employee_logout"
    ),

    path(
        "employee-dashboard/",
        views.employee_dashboard,
        name="employee_dashboard"
    ),

    path(
        "apply/",
        views.loan_application,
        name="loan_application"
    ),

    path(
        "status/",
        views.check_status,
        name="check_status"
    ),

    path(
        "success/",
        views.loan_success,
        name="loan_success"
    ),

    path(
        "loan-details/",
        views.loan_details,
        name="loan_details"
    ),

    path(
        "approve-loan/<int:loan_id>/",
        views.approve_loan,
        name="approve_loan"
    ),

    path(
        "reject-loan/<int:loan_id>/",
        views.reject_loan,
        name="reject_loan"
    ),

    path(
        "application-status/<int:loan_id>/",
        views.application_status,
        name="application_status"
    ),

]
