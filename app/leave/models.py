from datetime import datetime

from django.db import models
from django.urls import reverse
from users.models import User


class EmployeeLeave(models.Model):
    employee = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="employee"
    )
    leave_days_available = models.IntegerField(default=0)
    leave_days_taken = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("leave:employee-leave-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.employee.username}"


class LeaveRequest(models.Model):
    employee = models.ForeignKey(
        EmployeeLeave,
        on_delete=models.CASCADE,
        related_name="leave_requests",
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="updated_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    holidays = models.IntegerField(default=0)
    weekends = models.IntegerField(default=0)
    days_requested = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    @property
    def get_day_count(self):
        day_count = self.leave_end_date - self.leave_start_date
        return day_count.days

    @property
    def get_days_requested(self):
        holiday_weekend = (self.weekends * 2) + self.holidays
        days_requested = self.get_day_count - holiday_weekend
        return days_requested

    # def get_leave_days_available(self):
    #     return self.leave_days_available - self.leave_days_taken

    def save(self, *args, **kwargs):
        self.days_requested = self.get_days_requested
        super(LeaveRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.employee.username}"
