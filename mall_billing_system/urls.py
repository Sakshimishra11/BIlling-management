from django.contrib import admin
from django.urls import path
from mallbilling import views

urlpatterns = [
    path('', views.login, name='login'),
    path('billing/', views.billing, name='billing'),
    # path('save_bill/', views.save_bill, name='save_bill'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/create-product/', views.create_product, name='create_product'),
    path('employee/login/', views.employee_login, name='employee_login'),
    path('employee/billing/', views.billing, name='billing'),
    path('create-admin/', views.create_admin, name='create_admin'),
    path('admin/', admin.site.urls),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('employee/register/', views.register_employee, name='register_employee'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('get_product_price/', views.get_product_price, name='get_product_price'),
]
