from django.urls import path

from location import views

app_name = 'location'

urlpatterns = [
    path('', views.LocationView.as_view(), name='location_list'),
    path('add/', views.CreateLocationView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.delete_location, name='delete'),
    path('<int:pk>/activate/', views.activate_location, name='activate'),
]