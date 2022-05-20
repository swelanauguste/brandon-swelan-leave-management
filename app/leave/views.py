from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, UpdateView

from .models import EmployeeLeave, LeaveRequest


class EmployeeLeaveListView(ListView):
    model = EmployeeLeave


class EmployeeLeaveDetailView(DetailView):
    model = EmployeeLeave


class LeaveRequestListView(ListView):
    model = LeaveRequest


class LeaveRequestDetailView(DetailView):
    model = LeaveRequest
