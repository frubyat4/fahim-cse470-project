from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.urls import reverse, resolve
from GarmentsManagementApp.views import *
from .models import Garment, Department, Employee, Products, Order, Shipments, Supplier

#reponse - 200 - OK
#reponse - 302 - found
#reponse - 404 - Not found



class TestUrls(SimpleTestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePage.html')

    def test_abt(self):
        response = self.client.get('/aboutUs/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutUs.html')

    def test_collab(self):
        response = self.client.get('/collaboration/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'collaboration.html')

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEquals(response.status_code, 302)

    def test_dashboard(self):
        response = self.client.get('/dashboard/')
        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'dashboard.html')

    def test_addEmployee(self):
        response = self.client.get('/addEmployee/')
        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'AddEmployee.html')

    def test_showEmployee(self):
        response = self.client.get('/employees/')
        self.assertEquals(response.status_code, 302)

    def test_editEmployee(self):
        response = self.client.get('/editEmployee/<int:pk>/')
        self.assertEquals(response.status_code, 404)
        # self.assertTemplateUsed(response, 'EditEmployee.html')

    def test_deleteEmployees(self):
        response = self.client.get('/deleteEmployee/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_createProduct(self):
        response = self.client.get('/createproduct/')
        self.assertEquals(response.status_code, 302)

    def test_showProducts(self):
        response = self.client.get('/ShowProducts/')
        self.assertEquals(response.status_code, 302)

    def test_editProducts(self):
        response = self.client.get('/editProduct/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_deleteProducts(self):
        response = self.client.get('/deleteProduct/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_addGarment(self):
        response = self.client.get('/addGarment/')
        self.assertEquals(response.status_code, 302)

    def test_showGarment(self):
        response = self.client.get('/ShowGarments/')
        self.assertEquals(response.status_code, 302)

    def test_editGarment(self):
        response = self.client.get('/editGarment/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_createOrder(self):
        response = self.client.get('/createorder/')
        self.assertEquals(response.status_code, 302)

    def test_showOrder(self):
        response = self.client.get('/showorders/')
        self.assertEquals(response.status_code, 302)

    def test_deleteOrder(self):
        response = self.client.get('/deleteOrder/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_forward(self):
        response = self.client.get('/forward/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_reject(self):
        response = self.client.get('/reject/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_showDepartment(self):
        response = self.client.get('/showdepartments/')
        self.assertEquals(response.status_code, 302)

    def test_showSuppliers(self):
        response = self.client.get('/showSuppliers/')
        self.assertEquals(response.status_code, 302)

    def test_showShipments(self):
        response = self.client.get('/showShipments/')
        self.assertEquals(response.status_code, 302)

    def test_calculateDate(self):
        response = self.client.get('/calculateDate/')
        self.assertEquals(response.status_code, 302)


class TestModels(TestCase):

    @classmethod
    def setUp(cls):
        Garment.objects.create(name='cloth', type='leather')
        Department.objects.create(Name='Production', phone='1234', address='abcd', note='abcdefg')
        Employee.objects.create(EmployeeID='-1', Name='Fahim', department=Department.objects.get(id=1), salary='25',
                                Phone='123', address='abcd', status='active')
        Products.objects.create(product_id='-1', current_stock='10', garment=Garment.objects.get(id=1), Name='Shirt',
                                price='123', description='abcd', workingHoursPerItem='1')
        Order.objects.create(OrderID='-1', Status='abc', CustomerName='abc', CustomerPhn='123',
                             department=Department.objects.get(id=1), product=Products.objects.get(id=1), quantity='10',
                             TotalPrice='1000')
        Shipments.objects.create(product=Products.objects.get(id=1), order=Order.objects.get(id=1),
                                 delivaryDate='2020-01-01')
        Supplier.objects.create(name='abc', Company_Name='abc', Company_Address='abc', phone='123',
                                garment=Garment.objects.get(id=1), deliveryDate='2020-01-01')

    def test_Garment(self):
        garment = Garment.objects.get(id=1)
        expected_garment_name = garment.name
        expected_garment_type = garment.type
        self.assertEquals(expected_garment_name, 'cloth')
        self.assertEquals(expected_garment_type, 'leather')

    def test_Department(self):
        department = Department.objects.get(id=1)
        expected_department_Name = department.Name
        expected_department_phone = department.phone
        expected_department_address = department.address
        expected_department_note = department.note
        self.assertEquals(expected_department_Name, 'Production')
        self.assertEquals(expected_department_phone, '1234')
        self.assertEquals(expected_department_address, 'abcd')
        self.assertEquals(expected_department_note, 'abcdefg')

    def test_Employee(self):
        employee = Employee.objects.get(id=1)
        expected_employee_EmployeeID = employee.EmployeeID
        expected_employee_Name = employee.Name
        expected_employee_department = employee.department
        expected_employee_salary = employee.salary
        expected_employee_Phone = employee.Phone
        expected_employee_address = employee.address
        expected_employee_status = employee.status
        self.assertEquals(expected_employee_EmployeeID, -1)
        self.assertEquals(expected_employee_Name, 'Fahim')
        self.assertEquals(expected_employee_department, Department.objects.get(id=1))
        self.assertEquals(expected_employee_salary, 25)
        self.assertEquals(expected_employee_Phone, '123')
        self.assertEquals(expected_employee_address, 'abcd')
        self.assertEquals(expected_employee_status, 'active')

    def test_Products(self):
        products = Products.objects.get(id=1)
        expected_products_product_id = products.product_id
        expected_products_current_stock = products.current_stock
        expected_products_garment = products.garment
        expected_products_Name = products.Name
        expected_products_price = products.price
        expected_products_description = products.description
        expected_products_workingHoursPerItem = products.workingHoursPerItem
        self.assertEquals(expected_products_product_id, -1)
        self.assertEquals(expected_products_current_stock, 10)
        self.assertEquals(expected_products_garment, Garment.objects.get(id=1))
        self.assertEquals(expected_products_Name, 'Shirt')
        self.assertEquals(expected_products_price, 123)
        self.assertEquals(expected_products_description, 'abcd')
        self.assertEquals(expected_products_workingHoursPerItem, 1)

    def test_Order(self):
        order = Order.objects.get(id=1)
        expected_order_OrderID = order.OrderID
        expected_order_Status = order.Status
        expected_order_CustomerName = order.CustomerName
        expected_order_CustomerPhn = order.CustomerPhn
        expected_order_department = order.department
        expected_order_product = order.product
        expected_order_quantity = order.quantity
        expected_order_TotalPrice = order.TotalPrice
        self.assertEquals(expected_order_OrderID, -1)
        self.assertEquals(expected_order_Status, 'abc')
        self.assertEquals(expected_order_CustomerName, 'abc')
        self.assertEquals(expected_order_CustomerPhn, '123')
        self.assertEquals(expected_order_department, Department.objects.get(id=1))
        self.assertEquals(expected_order_product, Products.objects.get(id=1))
        self.assertEquals(expected_order_quantity, 10)
        self.assertEquals(expected_order_TotalPrice, 1000)

    def test_Shipments(self):
        shipment = Shipments.objects.get(id=1)
        expected_shipment_product = shipment.product
        expected_shipments_order = shipment.order
        expected_shipments_delivaryDate = shipment.delivaryDate
        self.assertEquals(expected_shipment_product, Products.objects.get(id=1))
        self.assertEquals(expected_shipments_order, Order.objects.get(id=1))
        self.assertEquals(expected_shipments_delivaryDate, datetime.date(2020, 1, 1))


    def test_Supplier(self):
        supplier = Supplier.objects.get(id=1)
        expected_supplier_name = supplier.name
        expected_supplier_Company_Name = supplier.Company_Name
        expected_supplier_Company_Address = supplier.Company_Address
        expected_supplier_phone = supplier.phone
        expected_supplier_garment = supplier.garment
        expected_supplier_deliveryDate = supplier.deliveryDate
        self.assertEquals(expected_supplier_name, 'abc')
        self.assertEquals(expected_supplier_Company_Name, 'abc')
        self.assertEquals(expected_supplier_Company_Address, 'abc')
        self.assertEquals(expected_supplier_phone, '123')
        self.assertEquals(expected_supplier_garment, Garment.objects.get(id=1))
        self.assertEquals(expected_supplier_deliveryDate, datetime.date(2020, 1, 1))


