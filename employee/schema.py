import graphene
from graphene import Argument
from graphene_django.types import DjangoObjectType
from .models import Employee



class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee






class Query(object):
    all_employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, id=graphene.ID())

    def resolve_all_employees(self, info, **kwargs):
        # Querying a list of Employee
        return Employee.objects.all()

    def resolve_employee(self, info, id):
        # Querying a single employee
        return Employee.objects.get(pk=id)




#**************************** Create Employee-Mutation ********************#


class CreateEmployee(graphene.Mutation):
    # Let's define the arguments we can pass the create method 👍
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        phone_no = graphene.String()
        email = graphene.String()
        description = graphene.String()
        status = graphene.Boolean()

    # What it returns 💸
    employee = graphene.Field(EmployeeType)

    # Where you really do all the mutation 🦁 🐉
    def mutate(self, info, username, first_name=None,last_name=None,
               phone_no=None, email=None, description=None,status=True):
        employee = Employee.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            email=email,
            description=description,
            status=status,
        )

        employee.save()
        # return an instance of the Mutation 🤷‍♀️
        return CreateEmployee(
            employee=employee
        )





#*******************Update Employee-Mutation ***************** #


class UpdateEmployee(graphene.Mutation):
    # The input arguments for this mutation
    class Arguments:
        id = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        phone_no = graphene.String()
        email = graphene.String()
        description = graphene.String()
        status = graphene.Boolean()

    # Let's define the response of the mutation
    employee = graphene.Field(EmployeeType)

    # Where you really do all the mutation 🦁 🐉
    def mutate(self, info,id, username, first_name=None,last_name=None,
               phone_no=None, email=None, description=None,status=None):

        employee = Employee.objects.get(pk=id)
        employee.first_name =  first_name if first_name is not None else employee.first_name
        employee.last_name =  last_name if last_name is not None else employee.last_name
        employee.username =  username if username is not None else employee.username
        employee.phone_no =  phone_no if phone_no is not None else employee.phone_no
        employee.email =  email if email is not None else employee.email
        employee.description =  description if description is not None else employee.description
        employee.status = status if status is not None else employee.status


        employee.save()

        # return an instance of the Mutation 🤷‍♀
        return UpdateEmployee(employee=employee)





#**************************** Delete Employee-Mutation ***************** #
class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, id):
        employee = Employee.objects.get(pk=id)
        if employee is not None:
            employee.delete()
        return DeleteEmployee(employee=employee)




class Mutation(graphene.ObjectType):


    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

