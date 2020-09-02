# Step 0:

# Here we define a function:
def this_functions_prints_stars():
    print('I will print stars!')
    print('**********')

# Here we call the function:
this_functions_prints_stars()























# Step 1:
def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)
















# Step 3:
def function_with_default_value(name, age=0, needs_stars=False):
    message = '{} is {} years old!'.format(name, age)
    print(message)

    if needs_stars:
        print('*****')

function_with_default_value('Nikita')
function_with_default_value('Alex', age=19)
function_with_default_value('Bob', age=40, needs_stars=True)























# Step 4:
def named_values(name=None, surname=None, patronimic=None):
    print('Full name: {} {} {}'.format(surname, name, patronimic))

named_values(name='Nikita', surname='Sobolev', patronimic='Andreevich')
named_values(surname='Petrov', patronimic='Ivanovich', name='Ivan')
named_values(surname='Semenov', name='Petr', patronimic='Ivanovich')
