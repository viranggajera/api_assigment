from app_apis import views
from django.urls import path

urlpatterns = [
    path('', views.Employee_List_API, name='Employee_List_API'),
    path('Employee_Detail_API/<int:employee_id>',
         views.Employee_Detail_API, name='Employee_Detail_API'),
]