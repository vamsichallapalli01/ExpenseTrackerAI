from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import FileResponse
from django.http import HttpResponse
from .models import UserProfile
from .forms import ProfileForm

from .models import RecurringExpense

from .forms import RecurringExpenseForm

import openpyxl
from .utils import create_pdf_report
from .models import Budget, Income, Expense
from .forms import RegisterForm, IncomeForm, ExpenseForm, BudgetForm


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")



@login_required
def dashboard(request):

    incomes = Income.objects.filter(
        user=request.user
    )

    expenses = Expense.objects.filter(
        user=request.user
    )

    current_month = date.today().month

    monthly_incomes = incomes.filter(
        date__month=current_month
    )

    monthly_expenses = expenses.filter(
        date__month=current_month
    )

    total_income = sum(
        income.amount
        for income in incomes
    )

    total_expense = sum(
        expense.amount
        for expense in expenses
    )

    savings = total_income - total_expense

    monthly_income_total = sum(
        income.amount
        for income in monthly_incomes
    )

    monthly_expense_total = sum(
        expense.amount
        for expense in monthly_expenses
    )

    monthly_savings = (
        monthly_income_total -
        monthly_expense_total
    )

    recent_expenses = expenses.order_by(
        '-date'
    )[:5]

    # Budget

    budget = Budget.objects.filter(
        user=request.user
    ).first()

    monthly_budget = 0
    remaining_budget = 0
    budget_percent = 0

    if budget:

        monthly_budget = (
            budget.monthly_budget
        )

        remaining_budget = (
            monthly_budget -
            total_expense
        )

        if monthly_budget > 0:

            budget_percent = min(

                round(

                    (
                        total_expense /
                        monthly_budget
                    ) * 100,

                    2

                ),

                100

            )

    # Analytics

    category_totals = {}

    for expense in expenses:

        if expense.category not in category_totals:

            category_totals[
                expense.category
            ] = 0

        category_totals[
            expense.category
        ] += expense.amount

    top_category = "No Data"

    if category_totals:

        top_category = max(

            category_totals,

            key=category_totals.get

        )

    largest_expense = expenses.order_by(
        '-amount'
    ).first()

    largest_expense_amount = 0

    if largest_expense:

        largest_expense_amount = (
            largest_expense.amount
        )

    average_expense = 0

    if expenses.exists():

        average_expense = round(

            total_expense /

            expenses.count(),

            2

        )

    total_transactions = (
        expenses.count()
    )

    # Pie Chart

    expense_categories = []
    expense_amounts = []

    for category, _ in Expense.CATEGORY_CHOICES:

        category_total = sum(

            expense.amount

            for expense in expenses.filter(
                category=category
            )

        )

        if category_total > 0:

            expense_categories.append(
                category
            )

            expense_amounts.append(
                float(category_total)
            )
        # Monthly Trend Data

    monthly_labels = []

    monthly_totals = []

    for month in range(1, 13):
        total = sum(

        expense.amount

        for expense in Expense.objects.filter(
            user=request.user,
            date__month=month
        )

    )

    monthly_labels.append(month)

    monthly_totals.append(
        float(total)
    )



    # Notifications

    notifications = []

    if budget_percent >= 90:

        notifications.append(

             "⚠ Budget usage is above 90%."

    )
    
    if remaining_budget < 0:

        notifications.append(

            "⚠ You exceeded your monthly budget."

    )
        
    if savings < 0:

        notifications.append(

            "⚠ Expenses exceed income."

    )
        
    if total_income == 0:

        notifications.append(

        "⚠ No income recorded."

    )
        
    if RecurringExpense.objects.filter(

    user=request.user

    ).exists():

        notifications.append(

            "ℹ Recurring expenses are active."

    )
    
    # AI Insights

    insights = []

    if top_category != "No Data":

        insights.append(

        f"Your largest spending category is {top_category}."

    )

    if total_income > 0:

        savings_percent = round(

        (savings / total_income) * 100,

        2

    )

    insights.append(

        f"You saved {savings_percent}% of your income."

    )
    if remaining_budget > 0:

        insights.append(

        f"You still have ${remaining_budget} remaining in your budget."

    )


    context = {

        'total_income': total_income,
        'total_expense': total_expense,
        'savings': savings,

        'recent_expenses': recent_expenses,

        'monthly_budget': monthly_budget,
        'remaining_budget': remaining_budget,
        'budget_percent': budget_percent,

        'monthly_income_total':
            monthly_income_total,

        'monthly_expense_total':
            monthly_expense_total,

        'monthly_savings':
            monthly_savings,

        'top_category':
            top_category,

        'largest_expense_amount':
            largest_expense_amount,

        'average_expense':
            average_expense,

        'total_transactions':
            total_transactions,

        'expense_categories':
            expense_categories,

        'expense_amounts':
            expense_amounts,

        'monthly_labels': monthly_labels,
        'monthly_totals': monthly_totals,

        'insights': insights,
        'notifications': notifications,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def add_income(request):

    if request.method == "POST":
        form = IncomeForm(request.POST)

        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')

    else:
        form = IncomeForm()

    return render(request, 'add_income.html', {'form': form})


@login_required
def add_expense(request):

    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')

    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


@login_required
def set_budget(request):

    budget = Budget.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)

        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('dashboard')

    else:
        form = BudgetForm(instance=budget)

    return render(request, 'budget.html', {'form': form})

@login_required
def reports(request):

    incomes = Income.objects.filter(
        user=request.user
    ).order_by('-date')

    expenses = Expense.objects.filter(
        user=request.user
    ).order_by('-date')

    category = request.GET.get(
        'category'
    )

    month = request.GET.get(
        'month'
    )

    if category:

        expenses = expenses.filter(
            category=category
        )

    if month:

        expenses = expenses.filter(
            date__month=month
        )

    context = {

        'incomes': incomes,
        'expenses': expenses,

        'categories':
            Expense.CATEGORY_CHOICES,

    }

    return render(
        request,
        'reports.html',
        context
    )

@login_required
def export_pdf(request):

    incomes = Income.objects.filter(
        user=request.user
    )

    expenses = Expense.objects.filter(
        user=request.user
    )

    total_income = sum(
        income.amount
        for income in incomes
    )

    total_expense = sum(
        expense.amount
        for expense in expenses
    )

    savings = (
        total_income -
        total_expense
    )

    pdf = create_pdf_report(
        total_income,
        total_expense,
        savings
    )

    return FileResponse(
        pdf,
        as_attachment=True,
        filename='finance_report.pdf'
    )


@login_required
def export_excel(request):

    workbook = openpyxl.Workbook()

    summary_sheet = workbook.active
    summary_sheet.title = "Summary"

    incomes = Income.objects.filter(
        user=request.user
    )

    expenses = Expense.objects.filter(
        user=request.user
    )

    total_income = sum(
        income.amount
        for income in incomes
    )

    total_expense = sum(
        expense.amount
        for expense in expenses
    )

    savings = (
        total_income -
        total_expense
    )

    # Summary Sheet

    summary_sheet.append(
        ["Expense Tracker Summary"]
    )

    summary_sheet.append([])

    summary_sheet.append(
        ["Total Income", float(total_income)]
    )

    summary_sheet.append(
        ["Total Expense", float(total_expense)]
    )

    summary_sheet.append(
        ["Savings", float(savings)]
    )

    # Income Sheet

    income_sheet = workbook.create_sheet(
        "Income"
    )

    income_sheet.append(
        ["Source", "Amount", "Date"]
    )

    for income in incomes:

        income_sheet.append([

            income.source,

            float(income.amount),

            str(income.date)

        ])

    # Expense Sheet

    expense_sheet = workbook.create_sheet(
        "Expenses"
    )

    expense_sheet.append([

        "Category",

        "Amount",

        "Date",

        "Description"

    ])

    for expense in expenses:

        expense_sheet.append([

            expense.category,

            float(expense.amount),

            str(expense.date),

            expense.description

        ])

    response = HttpResponse(

        content_type=

        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    )

    response[
        'Content-Disposition'
    ] = (

        'attachment; '

        'filename=finance_report.xlsx'

    )

    workbook.save(
        response
    )

    return response

@login_required
def profile(request):

    profile, created = (
        UserProfile.objects.get_or_create(
            user=request.user
        )
    )

    if request.method == "POST":

        form = ProfileForm(

            request.POST,

            request.FILES,

            instance=profile

        )

        if form.is_valid():

            form.save()

            return redirect(
                'profile'
            )

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(

        request,

        'profile.html',

        {

            'form': form,

            'profile': profile

        }

    )

@login_required
def recurring_expenses(request):

    expenses = RecurringExpense.objects.filter(

        user=request.user

    )

    return render(

        request,

        'recurring_expenses.html',

        {

            'expenses': expenses

        }

    )

@login_required
def add_recurring_expense(request):

    if request.method == "POST":

        form = RecurringExpenseForm(

            request.POST

        )

        if form.is_valid():

            expense = form.save(

                commit=False

            )

            expense.user = request.user

            expense.save()

            return redirect(

                'recurring_expenses'

            )

    else:

        form = RecurringExpenseForm()

    return render(

        request,

        'add_recurring_expense.html',

        {

            'form': form

        }

    )