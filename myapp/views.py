from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department, Designation, EmployeeType
from django.core.paginator import Paginator
from django.urls import reverse  # Import reverse


def home(request):
    employees = Employee.objects.all()  # Retrieve all employees
    return render(request, 'template.html', {'employees': employees})


def employee(request):
    employees = Employee.objects.all()  # Get all employees
    departments = Department.objects.all()
    designations = Designation.objects.all()
    employee_types = EmployeeType.objects.all()
    
    query = request.GET.get('query', '')
    if query:
        employees = employees.filter(name__icontains=query)  # Search by name

    paginator = Paginator(employees, 10)  # Paginate by 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'departments': departments,
        'designations': designations,
        'employee_types': employee_types,
        'query': query,
    }
    
    return render(request, 'home.html', context)

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        department_id = request.POST.get('department')
        designation_id = request.POST.get('designation')
        employee_type_id = request.POST.get('employee_type')
        joined = request.POST.get('joined')
        status = request.POST.get('status')

        department = Department.objects.get(dept_id=department_id)
        designation = Designation.objects.get(des_id=designation_id)
        employee_type = EmployeeType.objects.get(empt_id=employee_type_id)

        employee = Employee(
            name=name,
            age=age,
            department=department,
            designation=designation,
            employee_type=employee_type,
            joined=joined,
            status=status
        )
        employee.save()

        # Get current page number
        current_page = request.POST.get('page', 1)
        return redirect(f"{reverse('employee')}?page={current_page}")

    return redirect('employee')  # For GET requests, redirect to employee list

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.age = request.POST.get('age')
        department_id = request.POST.get('department')
        designation_id = request.POST.get('designation')
        employee_type_id = request.POST.get('employee_type')
        employee.joined = request.POST.get('joined')
        employee.status = request.POST.get('status')

        employee.department = Department.objects.get(dept_id=department_id)
        employee.designation = Designation.objects.get(des_id=designation_id)
        employee.employee_type = EmployeeType.objects.get(empt_id=employee_type_id)

        employee.save()

        # Get current page number
        current_page = request.POST.get('page', 1)
        return redirect(f"{reverse('employee')}?page={current_page}")

    # Provide context for the edit form
    departments = Department.objects.all()
    designations = Designation.objects.all()
    employee_types = EmployeeType.objects.all()

    context = {
        'edit_employee': employee,
        'departments': departments,
        'designations': designations,
        'employee_types': employee_types,
    }
    
    return render(request, 'home.html', context)

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()

        # Get current page number
        current_page = request.POST.get('page', 1)
        return redirect(f"{reverse('employee')}?page={current_page}")

    return redirect('employee')  # Redirect to the employee list for non-POST requests
