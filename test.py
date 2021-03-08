import unittest
from mock import patch,mock_open
import json
from employee_salaries import EmployeeSalaries
from custom_error.value_error import ValueException
class TestEmployeeSalariesFunctions(unittest.TestCase):

    def setUp(self):
        # initialize object
        self.obj = EmployeeSalaries()

    def test_averageAge(self):
        # test average age
        sample_data = [{'age':10 , 'salary':'£1000'},
                       {'age':20,'salary':'$2000'},
                       {'age':30,'salary':'$3000'}]
        expected_output =20
        output = self.obj.averageAge(sample_data)



        self.assertEqual(expected_output,output)




    def test_averageAgeErrorTest(self):
        # test validation in average age
        sample_data = [{ 'salary':'£1000'},
                       {'age':20,'salary':'$2000'},
                       {'age':30,'salary':'$3000'}]


        self.assertRaises(ValueException,self.obj.averageAge,sample_data)
        expected_exception = 'age value not present in some elemenets'
        self.assertRaises(ValueException,
            self.obj.averageAge,sample_data)

        expected_error = 'age value not present in some elemenets'
        try:
            output = self.obj.averageAge(sample_data)
        except ValueException as error:
            print(124)
            print(error)
            self.assertTrue(expected_exception in str(error))



    def test_averageSalaryeErrorTest(self):
        # test validation in average salary
        sample_data = [{ 'salary':'£1000'},
                       {'age':20},
                       {'age':30,'salary':'$3000'}]


        self.assertRaises(ValueException,self.obj.averageSalary,sample_data)
        expected_exception = 'salary value not present in some elemenets'
        self.assertRaises(ValueException,
            self.obj.averageSalary,sample_data)


        try:
            output = self.obj.averageSalary(sample_data)
        except ValueException as error:

            self.assertTrue(expected_exception in str(error))

    def test_averageSalary(self):
        # test average salary
        sample_data = [{'age':10 , 'salary':'£1000'},
                       {'age':20,'salary':'$2000'},
                       {'age':30,'salary':'$3000'}]
        expected_output = 2000
        output = self.obj.averageSalary(sample_data)

        self.assertEqual(expected_output,output)

    def test_computeMinSalary(self):
        # test compute minimunm ssalary
        sample_data = [{'age':10 , 'salary':'£1000'},
                       {'age':20,'salary':'$2000'},
                       {'age':30,'salary':'$3000'}]
        expected_output =[{'age': 10, 'salary': '£1000'}]
        output = self.obj.computeMinSalary(sample_data)

        self.assertEqual(expected_output,output)

    def test_computMaxSalary(self):
        sample_data = [{'age': 10, 'salary': '£1000'},
                       {'age': 20, 'salary': '$2000'},
                       {'age': 30, 'salary': '$3000'}]
        expected_output = [{'age': 30, 'salary': '$3000'}]
        output = self.obj.computMaxSalary(sample_data)

        self.assertEqual(expected_output, output)

    def test_computeAverageYearlyIncrease(self):
        sample_data = [{'age': 10, 'salary': '£1000'},
                       {'age': 20, 'salary': '$2000'},
                       {'age': 30, 'salary': '$3000'}]
        output = self.obj.computeAverageYearlyIncrease(sample_data,10,500)
        expected_output = 150



        self.assertEqual(expected_output, output)

    #mocking is done to avoid re-running of functions
    @patch('employee_salaries.EmployeeSalaries.computeAverageYearlyIncrease', return_value=150)
    @patch('employee_salaries.EmployeeSalaries.computMaxSalary', return_value=[{'age': 30, 'salary': '$3000'}])
    @patch('employee_salaries.EmployeeSalaries.computeMinSalary', return_value=[{'age': 10, 'salary': '£1000'}])
    @patch('employee_salaries.EmployeeSalaries.averageSalary', return_value=2000)
    @patch('employee_salaries.EmployeeSalaries.averageAge', return_value=20)
    def test_salaries(self,m1,m2,m3,m4,m5):
        sample_data = [{'age': 10, 'salary': '£1000'},
                       {'age': 20, 'salary': '$2000'},
                       {'age': 30, 'salary': '$3000'}]
        sample_age = 10
        sample_salary = 500

        output = self.obj.salaries(sample_data,sample_age,sample_salary)


        expected_output = json.dumps({
            'avg_age': 20,
            'avg_salary': 2000,
            'avg_yearly_increase': 150,
            'max_salary': [{'age': 30, 'salary': '$3000'}],
            'min_salary': [{'age': 10, 'salary': '£1000'}]
        })

        self.assertEqual(output,expected_output)



if __name__ == '__main__':
        unittest.main()