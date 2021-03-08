import math
import json
from multiprocessing import Pool
from custom_error.value_error import ValueException
from helper import extractAge,extractDigitFromSalary



class EmployeeSalaries:

    def __init__(self):
        self.pool = Pool()

    def computeAverageYearlyIncrease(self,data,age,salary):
        # Compute average yearly increase


        average_age_increase = self.averageAge(data) - age
        average_salary_increase = self.averageSalary(data) - salary

        yearly_avg_increase = math.floor(
            average_salary_increase / average_age_increase)

        return yearly_avg_increase


    def computMaxSalary(self,data):
        # Compute max salary
        salaries = self.process_salary(data)
        threshold = '$' + str(max(salaries))

        max_salary = [e for e in data if e['salary'] == threshold]
        return max_salary


    def computeMinSalary(self,data):
        # Compute min salary
        salaries = self.process_salary(data)
        min_salary = [e for e in data if e['salary'] ==
                      '£{}'.format(str(min(salaries)))]
        return min_salary

    def process_salary(self,data):
        # multiprocessing for creating salary_list
        salaries = self.pool.map(extractDigitFromSalary,data)

        return salaries

    def process_age(self,data):
        # multiprocessing for creating age_list
        age_list = self.pool.map(extractAge,data)

        return age_list

    def averageAge(self,data):
        '''
        Fetch average age
        :param data: List of dictionary
        :return: int
        '''
        age_list = self.process_age(data)

        #sum and divide len
        average_age = math.floor(sum(age_list)/len(data))
        return average_age


    def extractAge(self,data_element):
        """
        fetch age from dict
        :param data_element: dict
        :return: int
        """
        # validation
        if('age' not in data_element):
            raise ValueException('age value not present in some elemenets')
        return data_element['age']


    def averageSalary(self,data):
        '''
        Fetch average salary
        :param data: List of dictionary
        :return: int
        '''

        salaries = self.process_salary(data)
        # sum and divide len
        average_salary = math.floor(sum(salaries)/len(data))

        return average_salary


    def salaries(self, data, age, salary):
        # age and salary are the starting age and salary used to
        # compute the average yearly increase of salary.

        # Compute average yearly increase

        #try:
        yearly_avg_increase = self.computeAverageYearlyIncrease(data,age,salary)

        # Compute max salary
        max_salary = self.computMaxSalary(data)

        # Compute min salary
        min_salary = self.computeMinSalary(data)

        # compute average Age

        avg_age = self.averageAge(data)

        # compute average Salary
        avg_salary = self.averageSalary(data)

        return json.dumps({
            'avg_age': avg_age,
            'avg_salary': avg_salary,
            'avg_yearly_increase': yearly_avg_increase,
            'max_salary': max_salary,
            'min_salary': min_salary
        })

        '''
        except ValueException as e:
            return json.dumps({'error': str(e)})
        except Exception as e:
            return json.dumps({'error': str(e)})
        '''


if __name__=='__main__':
    obj = EmployeeSalaries()
    sample_data = [{'age': 10, 'salary': '£1000'},
                   {'age': 20, 'salary': '$2000'},
                   {'age': 30, 'salary': '$3000'}]
    sample_age = 10
    sample_salary = 500

    print(obj.salaries(sample_data,sample_age,sample_salary))