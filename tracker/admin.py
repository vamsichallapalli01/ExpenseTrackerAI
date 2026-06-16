from django.contrib import admin

from .models import Income
from .models import Expense
from .models import Budget


admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Budget)