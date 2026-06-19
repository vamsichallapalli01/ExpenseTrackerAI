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
      auth_views.LoginView.as_view(template_name='login.html'),
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
    path(
    'receipt/',
    views.upload_receipt,
    name='receipt'

    ),
    path(
    'send-report/',
    views.send_report,
    name='send_report'
    ),

    path(
    'api/income/',
    views.IncomeListAPI.as_view(),
    name='api_income'
    ),

    path(
    'api/expense/',
    views.ExpenseListAPI.as_view(),
    name='api_expense'
    ),

    path(
    'api/budget/',
    views.BudgetAPI.as_view(),
    name='api_budget'
    ),

    path(
    'api/dashboard/',
    views.DashboardAPI.as_view(),
    name='api_dashboard'
    ),

    path(
    'income/edit/<int:pk>/',
    views.edit_income,
    name='edit_income'
    ),

    path(
    'income/delete/<int:pk>/',
    views.delete_income,
    name='delete_income'
    ),

    path(
    'expense/edit/<int:pk>/',
    views.edit_expense,
    name='edit_expense'
    ),

    path(
    'expense/delete/<int:pk>/',
    views.delete_expense,
    name='delete_expense'
    ),
    path(
    'income/list/',
    views.income_list,
    name='income_list'
    ),
    path(
    'expense/list/',
    views.expense_list,
    name='expense_list'
    ),
    path(
    'backup/',
    views.backup_data,
    name='backup_data'
    ),
    path(
    'restore/',
    views.restore_data,
    name='restore_data'
    ),
]