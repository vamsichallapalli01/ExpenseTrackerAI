from rest_framework import serializers
from .models import Income
from .models import Expense
from .models import Budget


class IncomeSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Income

        fields = '__all__'

class ExpenseSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Expense

        fields = '__all__'

class BudgetSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Budget

        fields = '__all__'

