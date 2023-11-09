from django.urls import path

from timesheet import views

app_name = 'timesheet'

urlpatterns = [
    path('start_timesheet/', views.new_timesheet, name='start_timesheet'),
    path('stop_timesheet/', views.stop_timesheet, name='stop_timesheet'),
]
