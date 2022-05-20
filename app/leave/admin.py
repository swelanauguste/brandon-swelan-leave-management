from django.contrib import admin

from .models import EmployeeLeave, LeaveRequest

admin.site.register(EmployeeLeave)
admin.site.register(LeaveRequest)