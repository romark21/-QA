# coding: utf8
"""
                                    Task №1
  Write a program that takes two integers (a and b) as input and performs the following actions with them:
- compares these two numbers and returns the result of the comparison by outputting to the console one of the options:
"a > b", "a < b" or "a = b";
- performs addition, subtraction, division and multiplication operations with these numbers and outputs the result to
the console.


                                      Task №2
  Write a program that takes two strings (a and b) as input and compares them. As a result of the comparison in the
console should display one of the messages: "Strings are non-identical" or "Strings are identical"



                                      Task №3
  Write a program that takes a number as input and outputs to the console all the
even numbers in the range of the entered number (inclusive).
"""


#  Запустить код, затем следовать командам в консоли.
#  Run the code, then follow the commands in the console

class Task1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compares_two_numbers(self):
        if self.a > self.b:
            return f'{self.a} > {self.b}'
        elif self.a < self.b:
            return f'{self.a} < {self.b}'
        else:
            return f'{self.a} = {self.b}'

    def additions_numbers(self):
        return f'{self.a} + {self.b} = {self.a + self.b}'

    def subtraction_numbers(self):
        return f'{self.a} - {self.b} = {self.a - self.b}'

    def division_numbers(self):
        if self.b == 0:
            return f'Division by zero, impossible!'
        else:
            return f'{self.a} : {self.b} = {self.a / self.b}'

    def multiplication_numbers(self):
        return f'{self.a} * {self.b} = {self.a * self.b}'


class Task2:
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def compares_two_strings(self):
        if self.string_1 == self.string_2:
            return 'The strings are identical!'
        else:
            return 'The strings are non-identical!'


class Task3:

    def __init__(self, num):
        self.num = num

    def __generate_list__(self):
        result = [_ for _ in range(self.num + 1)]
        return result

    def even_numbers(self):
        generated_list = self.__generate_list__()

        return (num for num in generated_list if num % 2 == 0)


def run_code():
    separate = '----' * 30
    choice_of_task = int(input('Which task do you want to do?\n'
                               '1 - Task №1\n'
                               '2 - Task №2\n'
                               '3 - Task №3\n'
                               'Enter the command number: '))
    print(separate)
    if choice_of_task == 1:
        try:
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            task_1 = Task1(a, b)
            print(task_1.compares_two_numbers())
            print(task_1.additions_numbers())
            print(task_1.subtraction_numbers())
            print(task_1.division_numbers())
            print(task_1.multiplication_numbers())
        except ValueError:
            print('Error! Enter a number or the field must not be empty.')

    elif choice_of_task == 2:
        string_1 = input('Enter the first string: ')
        string_2 = input('Enter the second string: ')
        task_2 = Task2(string_1, string_2)
        print(task_2.compares_two_strings())

    elif choice_of_task == 3:
        a = int(input('Enter a number that is a range of even numbers.\n'
                      'The search is performed from 0 to the value you entered (inclusive): '))
        task_3 = Task3(a)
        print(f'Even numbers are:', *task_3.even_numbers())

    else:
        print('There is no such command! Enter: 1, 2 or 3')


if __name__ == "__main__":
    run_code()
