from custom_error.value_error import ValueException

def extractDigitFromSalary(data_element):
    """
    fetch salary from dict
    :param data_element: dict
    :return: int
    """

    # validation
    if ('salary' not in data_element):
        raise ValueException('salary value not present in some elemenets')
    return int(data_element['salary'][1:])

def extractAge(data_element):
        """
        fetch age from dict
        :param data_element: dict
        :return: int
        """
        # validation
        if('age' not in data_element):
            raise ValueException('age value not present in some elemenets')
        return data_element['age']