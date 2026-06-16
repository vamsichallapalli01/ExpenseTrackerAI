from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path(
    "",
    views.dashboard,
    name="dashboard"
    ),

    path('login/',
      auth_views.LoginView.as_view(template_name='tracker/login.html'),
      name='login'
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
    'income/add/',
    views.add_income,
    name='add_income'
    ),

    path(
    'expense/add/',
    views.add_expense,
    name='add_expense'
    ),

    path("logout/", 
    views.logout_view, 
    name="logout"
    ),
    
    path(
    'budget/',
    views.set_budget,
    name='budget'
    ),

    path(
    'reports/',
    views.reports,
    name='reports'
    ),

    path(
    'export/pdf/',
    views.export_pdf,
    name='export_pdf'
    ),

    path(
    'export/excel/',
    views.export_excel,
    name='export_excel'
    ),

    path(
    'profile/',
    views.profile,
    name='profile'
    ),

    path(
    'recurring/',
    views.recurring_expenses,
    name='recurring_expenses'
    ),

    path(
    'recurring/add/',
    views.add_recurring_expense,
    name='add_recurring_expense'

  ),
]