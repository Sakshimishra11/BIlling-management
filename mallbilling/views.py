# mallbilling/views.py
from decimal import Decimal
from django.http import JsonResponse,HttpResponse,HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render
from django.contrib import messages
from .forms import AdminCreationForm,ProductForm,EmployeeRegistrationForm,CustomerForm
from django.shortcuts import render, redirect
from .models import Product, Admin, Employee





# FUNCTION 1....................//////////////////////////
def employee_login(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        try:
            employee = Employee.objects.get(employee_id=employee_id, password=password)
            request.session['employee_id'] = employee_id
            return redirect('billing')
        except Employee.DoesNotExist:
            error_message = 'Invalid employee credentials'
            return render(request, 'employee_login.html', {'error_message': error_message})
    return render(request, 'employee_login.html')

# FUNCTION 2....................//////////////////////////
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_login')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'register_employee.html', {'form': form})

# FUNCTION 3....................//////////////////////////
def create_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AdminCreationForm()
    return render(request, 'create_admin.html', {'form': form})
# FUNCTION 4....................//////////////////////////
def login(request):
    if request.method == 'POST':
        admin_id = request.POST['admin_id']
        password = request.POST['password']
        try:
            admin = Admin.objects.get(admin_id=admin_id, password=password)
            request.session['admin_id'] = admin_id
            return redirect('admin_dashboard')
        except Admin.DoesNotExist:
            error_message = 'Invalid admin credentials'
            messages.error(request, error_message)  # Add error message
            return render(request, 'login.html')
    return render(request, 'login.html')


# UNCTION 4....................//////////////////////////
def admin_dashboard(request):
    admin_id = request.session.get('admin_id')
    if admin_id:
        admin = Admin.objects.filter(admin_id=admin_id).first()
        products = Product.objects.all()
        return render(request, 'admin_dashboard.html', {'admin': admin, 'products': products})
    return redirect('login')

# FUNCTION 5....................//////////////////////////
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('admin_dashboard')
# FUNCTION 6....................//////////////////////////
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})


# FUNCTION 7....................//////////////////////////
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        product = Product(name=name, price=price)
        product.save()
        return redirect('admin_dashboard')
    return render(request, 'create_product.html')

# FUNCTION 8....................//////////////////////////

def billing(request):
    employee_id = request.session.get('employee_id')
    if employee_id:
        employee = Employee.objects.get(employee_id=employee_id)
        products = Product.objects.all()
        # Implement your billing logic here
        return render(request, 'billing.html', {'employee': employee, 'products': products})
    return redirect('employee_login')

# FUNCTION 9....................//////////////////////////
def get_product_price(request):
    product_id = request.GET.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
        price = product.price
    except Product.DoesNotExist:
        price = 0
    return JsonResponse({'price': price})

from decimal import Decimal


# FUNCTION 10.....................//////////////////////////
from django.shortcuts import render

from django.http import JsonResponse

def generate_bill(request):
    if request.method == 'POST':
        # Retrieve form data
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_mobile = request.POST.get('customer_mobile')
        product_ids = request.POST.getlist('product_ids[]')
        quantities = request.POST.getlist('quantities[]')

        # Perform validation on the data
        errors = []
        if not customer_name:
            errors.append("Please enter Customer name.")
        if not customer_email:
            errors.append("Please enter Customer email.")
        if not customer_mobile:
            errors.append("Please enter Customer Phone Number.")
        if len(product_ids) == 0:
            errors.append("Your cart is empty. Please add items to generate a bill.")

        if errors:
            return JsonResponse({'success': False, 'message': ', '.join(errors)}, status=422)

        total = Decimal('0.00')
        products = []

        for product_id, quantity in zip(product_ids, quantities):
            try:
                product = Product.objects.get(id=product_id)
                price = product.price
                subtotal = price * Decimal(quantity)
                total += subtotal

                products.append({
                    'name': product.name,
                    'price': price,
                    'quantity': quantity,
                    'subtotal': subtotal,
                })
            except Product.DoesNotExist:
                # Handle product not found
                pass

        bill_data = {
            'customer_name': customer_name,
            'customer_email': customer_email,
            'customer_mobile': customer_mobile,
            'products': products,
            'total': total,
        }
        return JsonResponse({'success': True, 'bill_data': bill_data})

        # return render(request, 'bill.html', {'bill_data': bill_data})

    else:
        return HttpResponseBadRequest('Invalid request method')


















