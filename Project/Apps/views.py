from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'staff':
        return redirect('staff_dashboard')
    elif user.role == 'customer':
        return redirect('customer_dashboard')
    return redirect('login')


def orders(request):
    return render(request, 'Apps/orders.html')

def kitchens(request):
    return render(request, 'Apps/kitchens.html')

def brands(request):
    return render(request, 'Apps/brands.html')

def payments(request):
    return render(request, 'Apps/payments.html')

def menu(request):
    return render(request, 'Apps/menu.html')

def inventory(request):
    return render(request, 'Apps/inventory.html')

def staff(request):
    return render(request, 'Apps/staff.html')
def admin_dashboard(request):
    return render(request, 'Apps/admin_dashboard.html')

def staff_dashboard(request):
    return render(request, 'Apps/staff_dashboard.html')

def customer_dashboard(request):
    return render(request, 'Apps/customer_dashboard.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.role == 'admin':
                return redirect('admin_dashboard')   # URL name for admin page
            elif user.role == 'staff':
                return redirect('staff_dashboard')   # URL name for staff page
            elif user.role == 'customer':
                return redirect('customer_dashboard')  # URL name for customer page
            else:
                messages.error(request, "User role undefined.")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'Apps/login.html')
@login_required
def admin_dashboard(request):
    return render(request, 'Apps/admin_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'Apps/staff_dashboard.html')

@login_required
def customer_dashboard(request):
    return render(request, 'Apps/customer_dashboard.html')
