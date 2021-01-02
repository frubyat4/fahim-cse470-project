from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.urls import reverse, resolve
from GarmentsManagementApp.views import *
from GarmentsManagementApp.models import Garment, Department, Employee, Products, Order, Shipments, Supplier

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
        Supplier.objects.create(name='abc', Company_Name='abc', Company_Address='abc', phone='123', garment=Garment.objects.get(id=1), deliveryDate='2020-01-01')

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
