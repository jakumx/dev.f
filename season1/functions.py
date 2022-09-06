from time import sleep


# 1.
def find_max_value(num1, num2, num3):
    """  Write a Python function to find the Max of three numbers. """
    numbers = (num1, num2, num3)
    max_number = 0
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
  
print('1. Valor maximo: ', find_max_value(1,2,3))

# 2. 
def sum_all_numbers(*numbers):
    """ Write a Python function to sum all the numbers in a list. """
    total = 0
    for num in numbers:
        total += num
    return total

print('2. suma de nums: ', sum_all_numbers(1,2,3,4,5,6,7,8,9,10))

# 3. 
def multiply_all_numbers(*numbers):
    """ Write a Python function to multiply all the numbers in a list. """
    total = 1
    for num in numbers:
        total *= num
    return total
  
print('3. multi de num: ', multiply_all_numbers(1,2,3,4,5,6,7,8,9,0))

# 4.
def reserse_string(word):
    """ Write a Python program to reverse a string. """
    reverse_word = ''
    for char_value in word:
        reverse_word = char_value + reverse_word
    return reverse_word

print('4. al reves: ', reserse_string('hello world'))

# 5.
def factorial_number(number): 
    """  Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. """
    if (number < 0):
        print('no puede ser menor que cero')
        return
    if (number == 0):
        return 0
    total = 1
    for num in range(1, number + 1):
        total *= num
    return total

print('5. factorial: ', factorial_number(3))

# 6. 
def number_in_range(number):
    """ Write a Python function to check whether a number falls in a given range. """
    return number > 0 and number < 10

print('6: dentro de rango 0-10', number_in_range(9))

# 7.
def uppers_lowers(word):
    """ Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. """
    upper = 0
    lower = 0
    for char in word:
        if (char.isupper()):
            upper += 1
        elif (char.islower()):
            lower += 1
    return (upper, lower)
  
print('7. mays , minus: ', uppers_lowers('The quick Brow Fox'))

# 8. 
def unique_list(number_list):
    """ Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
    Sample List : [1,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
    """
    definitive_list = []
    for number in number_list:
        if (number not in definitive_list):
            definitive_list.append(number)
    return definitive_list
  
print('8. lista unica: ', unique_list([1,2,3,3,3,3,4,5]))

# 9. 
def is_prime(number):
    """ Write a Python function that takes a number as a parameter and check the number is prime or not.  """
    count = 0
    for value_number in range(0, number + 1):
        if (value_number == 0):
            continue
        elif (number % value_number == 0):
            count += 1
    return count == 2
    
print('9. es numero primo: ', is_prime(11))

# 10. 
def even_numbers(numbers):
    """ Write a Python program to print the even numbers from a given list """
    even_list = []
    for number in numbers:
        if (number % 2 == 0):
            even_list.append(number)
    return even_list

print('10. numeros pares:', even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 11. 
def is_perfect(number):
    """ Write a Python function to check whether a number is perfect or not. """
    divisors = ()
    for value_number in range(1, number):
        if (number % value_number == 0):
            divisors += (value_number,)
    return sum_all_numbers(*divisors) == number

print('11. numero perfecto: ', is_perfect(5))

# 12. 
def remove_spaces(word):
    new_word = ''
    for char in word:
        if (char != ' '):
            new_word += char
    return new_word

def is_palindrome(word):
    """ Write a Python function that checks whether a passed string is palindrome or not. """
    return remove_spaces(reserse_string(word)) == remove_spaces(word)
  
print('12. es palindroma: ', is_palindrome('anita lava la tina'))

# 13.
def pascal_triangle(num_rows):
    """ Write a Python function that prints out the first n rows of Pascal's triangle """
    rows = [[1], [1,1]]
    if (num_rows == 0):
        return []
    if (num_rows == 1):
        return [[1]]
    if (num_rows == 2):
        return rows
    if (num_rows > 2):
        for row in range(3, num_rows + 1):
            row_to_add = []
            for index in range(0, row):
                if (index == 0):
                    row_to_add.append(1)
                elif (index == (row - 1)):
                    row_to_add.append(1)
                else:
                    row_to_add.append(rows[-1][index - 1] + rows[-1][index])
            rows.append(row_to_add)
        return rows

print('13. triangulo de pascal: ', pascal_triangle(6))

# 14.
def is_pangram(word):
    """  Write a Python function to check whether a string is a pangram or not. """
    for n in range(ord("a"), ord("z") + 1):
        if chr(n) not in word:
            return False
    return True

print('14. es pangram: ', is_pangram('The quick brown fox jumps over the lazy dog'))
print('14. es pangram: ', is_pangram('this is not a pangram'))

# 15.
def split_words(word_to_split):
    word_to_append = ''
    for index, char in enumerate(word_to_split):
        if index == len(word_to_split) - 1:
            word_to_append += char
            yield word_to_append
            word_to_append = ''
        elif char != '-':
            word_to_append += char
        else:
            yield word_to_append
            word_to_append = ''

def join_words(tuple_words):
    single_str = ''
    for index, word_ord in enumerate(tuple_words):
        single_str += word_ord[0]
        if index != len(tuple_words) - 1:
            single_str += '-'
    return single_str

def sort_words(words):
    """ Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
    Sample Items : green-red-yellow-black-white
    Expected Result : black-green-red-white-yellow
    """
    words_list = split_words(words)
    sorted_words = []
    for index_word_list, word in enumerate(words_list):
        first_letter_word_num = ord(word[0])
        if index_word_list == 0:
            sorted_words.append((word, first_letter_word_num))
        else:
            for index_sorted_word, word_sorted_words in enumerate(sorted_words):
                before_sorted_word_num = word_sorted_words[1]
                if first_letter_word_num > before_sorted_word_num and index_sorted_word == len(sorted_words) - 1:
                    sorted_words.append((word, first_letter_word_num))
                elif first_letter_word_num < before_sorted_word_num:
                    sorted_words.insert(index_sorted_word, (word, first_letter_word_num))
                    break
    return join_words(sorted_words)

print('15. ordenamiento de palabras: ', sort_words("green-red-yellow-black-white"))

# 16.
def squares_numbers(min_value = 1, max_value = 30):
    """16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). """
    if min_value < 1 or min_value >= max_value:
        print('min_value no puede ser menor que 1 o mayor o igual que max_value')
        return
    if max_value > 30 or max_value < min_value:
        print('max_value no puede ser mayor que 30 o menor o igual que min_value')
        return
    for value in range(min_value, max_value + 1):
        yield value ** value
    
print('16. cuadrados de numeros:', end=' ')
for square_number in squares_numbers():
    print(square_number, end='\033[0m')
print('')

# 17
def text_decorators():
    """17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python."""
    decorators_chain = [
        ('blue', '\033[94m'),
        ('bold', '\033[1m'),
        ('italics', '\033[3m'),
        ('underline', '\033[4m')]
    str_decorators = ''
    for decorator_tuple in decorators_chain:
        str_decorators += decorator_tuple[1] + decorator_tuple[0] + ' '
    return str_decorators

print('17. decoradores:', text_decorators(), sep=' ', end='\033[0m \n')

# 18.
def string_contains(str_to_validate, word):
    """18. Write a Python program to execute a string containing Python code."""
    word_included = ''
    for char_word in word:
        future_char_word = word_included + char_word
        if future_char_word == str_to_validate:
            return True
        if future_char_word[len(future_char_word) -1] == str_to_validate[len(future_char_word) -1]:
            word_included += char_word
        else:
            word_included = ''    
    return False

print('18. palabra incluida:', string_contains('yellow', 'green-red-yellow-black-white'))

# 19.
def funtion_inside():
    """19. Write a Python program to access a function inside a function."""
    def child_function():
        return 'child funtion'
    return child_function

print('19 funcion hija: ', funtion_inside()())

# 20.
def detect_loca_variables():
    """20. Write a Python program to detect the number of local variables declared in a function."""
    var_one = '1'
    var_two = '2'
    var_three = 'tree'
    return None

print(detect_loca_variables.__code__.co_nlocals)

# 21.
def execute_after_n_milliseconds(function, milliseconds):
    """21. Write a Python program that invoke a given function after specific milliseconds."""
    sleep(milliseconds / 1000)
    return function()

def hello_word():
    print('hello word')

print('21. invoca despues de milisegundos:',)
execute_after_n_milliseconds(hello_word, 1000)

