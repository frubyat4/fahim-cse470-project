from django.test import TestCase
from django.test import SimpleTestCase
from django.shortcuts import reverse
from django.urls import reverse, resolve
from GarmentsManagementApp.views import *


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


