from django.urls import path

from apps.management import views
from apps.management.views import CreateCustomer, CustomerList, CustomerUpdate, CustomerDelete

urlpatterns = [
    path('employ', views.emplo),
    path('manage', CreateCustomer.as_view(), name='create-employ'),
    path('manage/list', CustomerList.as_view(), name='create-employ-list'),
    path('manage_update/<int:pk>/', CustomerUpdate.as_view(), name='employ-update'),
    path('manage_delete/<int:pk>/', CustomerDelete.as_view(), name='employ-delete'),



]