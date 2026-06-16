from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import RecurringExpense
from .models import (
    Income,
    Expense,
    Budget
)


class RegisterForm(UserCreationForm):

    email = forms.EmailField(

        widget=forms.EmailInput(

            attrs={

                'class': 'form-control'

            }

        )

    )

    class Meta:

        model = User

        fields = [

            'username',

            'email',

            'password1',

            'password2'

        ]

    def __init__(

        self,

        *args,

        **kwargs

    ):

        super().__init__(

            *args,

            **kwargs

        )

        self.fields[
            'username'
        ].widget.attrs.update({

            'class':
            'form-control'

        })

        self.fields[
            'password1'
        ].widget.attrs.update({

            'class':
            'form-control'

        })

        self.fields[
            'password2'
        ].widget.attrs.update({

            'class':
            'form-control'

        })


class IncomeForm(forms.ModelForm):

    class Meta:

        model = Income

        fields = [
            'source',
            'amount',
            'date'
        ]

        widgets = {

            'source': forms.TextInput(

                attrs={
                    'class': 'form-control'
                }

            ),

            'amount': forms.NumberInput(

                attrs={
                    'class': 'form-control'
                }

            ),

            'date': forms.DateInput(

                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }

            )

        }


class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = [

            'category',
            'amount',
            'date',
            'description'

        ]

        widgets = {

            'category': forms.Select(

                attrs={

                    'class': 'form-select'

                }

            ),

            'amount': forms.NumberInput(

                attrs={

                    'class': 'form-control',

                    'placeholder':
                    'Expense Amount'

                }

            ),

            'date': forms.DateInput(

                attrs={

                    'class': 'form-control',

                    'type': 'date'

                }

            ),

            'description': forms.TextInput(

                attrs={

                    'class': 'form-control',

                    'placeholder':
                    'Description'

                }

            )

        }


class BudgetForm(forms.ModelForm):

    class Meta:

        model = Budget

        fields = [

            'monthly_budget'

        ]

        widgets = {

            'monthly_budget':

            forms.NumberInput(

                attrs={

                    'class': 'form-control',

                    'placeholder':
                    'Monthly Budget'

                }

            )

        }

class ProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'profile_picture'
        ]

class RecurringExpenseForm(

    forms.ModelForm

):

    class Meta:

        model = RecurringExpense

        fields = [

            'name',

            'amount',

            'frequency'

        ]

        widgets = {

            'name': forms.TextInput(

                attrs={

                    'class': 'form-control',

                    'placeholder':
                    'Expense Name'

                }

            ),

            'amount': forms.NumberInput(

                attrs={

                    'class': 'form-control'

                }

            ),

            'frequency': forms.Select(

                attrs={

                    'class': 'form-select'

                }

            )

        }


    class Meta:

        model = Income

        fields = [

            'source',
            'amount',
            'date'

        ]

        widgets = {

            'source': forms.TextInput(

                attrs={
                    'class': 'form-control'
                }

            ),

            'amount': forms.NumberInput(

                attrs={
                    'class': 'form-control'
                }

            ),

            'date': forms.DateInput(

                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }

            )

        }