from django.test import TestCase,SimpleTestCase
from  .models import Employee
from graphene.test import Client
from mixer.backend.django import mixer
import pytest
from ems.schema import schema

class EmployeeTestCase(TestCase):


    def setUp(self):
        Employee.objects.create(username="lion",first_name="king",last_name="raj",
                                phone_no="8978545",
                                email="raj@gmail.com",status=True)
        Employee.objects.create(username="hor",first_name="tr",last_name="ty",
                                phone_no="845597854",email="hor@gmail.com",status=True)




    def test_employee_data(self):
        """test employee  data"""
        obj = Employee.objects.get(username="lion")
        obj1 = Employee.objects.get(username="hor")
        self.assertEqual(obj.username, 'lion')
        self.assertEqual(obj1.username, 'hor')

    def test_employee_email(self):

        ''' test employee email'''
        obj = Employee.objects.get(email="raj@gmail.com")
        obj1 = Employee.objects.get(email="hor@gmail.com")
        self.assertEquals(obj.email,'raj@gmail.com')
        self.assertEquals(obj1.email,'hor@gmail.com')


    def test_employee_phone_no(self):

         ''' test employee phone no'''
         obj = Employee.objects.get(phone_no=8978545)
         obj1= Employee.objects.get(phone_no=845597854)
         self.assertEquals(obj.phone_no, '8978545')
         self.assertEquals(obj1.phone_no, '845597854')

#




#
employee_list_query = """
    query {
        allEmployees {
              id
              firstName
              lastName
              username
              phoneNo
              email
              status
              description
        }
    }
"""





single_employee_query = """
    query($id:ID!)
    {
        employee(id:$id) {
              id
              firstName
              lastName
              username
              phoneNo
              email
              status
              description
            
     }
    }
"""




create_employee_mutation = """
       mutation CreateEmployee($firstName:String,$lastName:String,$username:String,$phoneNo:String,$email:String,$status:Boolean,$description:String) {
        createEmployee(firstName: $firstName,lastName: $lastName,username: $username,phoneNo: $phoneNo,email: $email,status: $status,
                          description: $description) {
            employee {
              id
              firstName
              lastName
              username
              phoneNo
              email
              status
              description

        }
    }
}



"""



update_employee_mutation = """
       mutation UpdateEmployee($id:ID!$username:String,$description:String) {
        updateEmployee(id:$id,username:$username,description: $description) {
            employee {
              id
              firstName
              lastName
              username
              phoneNo
              email
              status
              description

        }
    }
}



"""





delete_employee_mutation = """
    mutation DeleteEmployee($id:ID!) {
        deleteEmployee(id:$id){
            employee{
              username
              firstName
              lastName
              email
              status
              description
              phoneNo
        }
        }
    }
"""


# print(employee_list_query,'dfds')
# ********** Test Employee Schema ******************** #
@pytest.mark.django_db
class TestEmployeeSchema(TestCase):

   #********** Setup Query and Mutation ************#
    def setUp(self):

        self.client = Client(schema)
        self.employee = mixer.blend(Employee)



   #***** Single Employee Query *******#
   #**** Employee id *******#
    def test_single_employee_query(self):
        response = self.client.execute(single_employee_query, variables={"id": self.employee.id})
        response_employee = response.get("data").get("employee")
        # print(response_employee,'ewrwcs')
        assert response_employee["id"] == str(self.employee.id)


   #*****  Employee list Query *******#
   #**** Employee List *******#
    def test_employee_list_query(self):
        mixer.blend(Employee)
        mixer.blend(Employee)

        response = self.client.execute(employee_list_query)
        # print(response,'dataeeer')
        allEmployees = response.get("data").get("allEmployees")
        ok = response.get("data").get("ok")
        # print(len(allEmployees),'length')
        assert len(allEmployees)




#*********** Employee mutation Creation ************#
### ***** Create Employee *****####

    def test_create_employee(self):

       employee = mixer.blend(Employee)

       response = self.client.execute(create_employee_mutation,
                        variables={"firstName":"ramesh",
                                   "lastName":"kannan",
                                   "username":"rameshkannan",
                                   "email":"rameshkannan@gmail.com",
                                   "phoneNo":"9147894561",
                                   "status":True,
                                   "description":"Wervfddgdgfgfg"

                                  })
       employee = response.get("data").get("createEmployee").get("employee")
       assert len(employee)
       username = employee.get("username")
       email = employee.get("email")
       assert username == employee['username']
       assert email == employee['email']




#************** Update mutation Testing *************#####

    def test_update_employee(self):

       employee = mixer.blend(Employee)

       response = self.client.execute(update_employee_mutation,
                                      variables={
                                           "id":self.employee.id,
                                           "username":"Gandhi",
                                           "description":"solution"
                                       })
       response_employee = response.get("data").get("updateEmployee").get("employee")
       username = response_employee.get("username")
       assert username == response_employee["username"]
       assert username != self.employee.username



## ******** Delete Mutation Testing *********#

    def test_delete_employee(self):
        response = self.client.execute(delete_employee_mutation, variables={"id": self.employee.id})
        ok = response.get("data").get("deleteEmployee").get("employee")
        assert ok
