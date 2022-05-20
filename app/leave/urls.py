from django.urls import path

from . import views

app_name = "leave"

urlpatterns = [
    path(
        "employee-leave",
        views.EmployeeLeaveListView.as_view(),
        name="employee-leave-list",
    ),
    path(
        "employee-leave/<int:pk>/",
        views.EmployeeLeaveDetailView.as_view(),
        name="employee-leave-detail",
    ),
    path(
        "leave-request",
        views.LeaveRequestListView.as_view(),
        name="leave-request-list",
    ),
    path(
        "leave-request/<int:pk>/",
        views.LeaveRequestDetailView.as_view(),
        name="leave-request-detail",
    ),
]
