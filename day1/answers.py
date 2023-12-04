import re

def answer1():
    list_of_digits = []
    #https://www.w3schools.com/python/python_file_open.asp
    calibration_values = open("day1/input.txt", "r")
    for values in calibration_values: 
       #https://stackoverflow.com/questions/32571348/getting-only-the-first-number-from-string-in-python
        first_digit = re.search(r'\d', values).group()
       #https://stackoverflow.com/questions/5320525/regular-expression-to-match-last-number-in-a-string
        last_digit = re.search(r'(\d)(?!.*\d)', values).group()
        concatenate = first_digit + last_digit
        list_of_digits.append(int(concatenate))
    #https://realpython.com/python-f-strings/    
    print(f'The sum of all calibration values for part 1 is {sum(list_of_digits)}')
answer1()

#COMPLETELY READ THE QUESTION WRONG ;-; THE ANSWER DOESN'T MAKE SENSE AS THERE ARE QUITE A FEW WORDED DIGITS MISSING
def answer2():
    list_of_digits = []
    calibration_values = open("day1/input.txt", "r")
    for values in calibration_values:
        all_worded_digits = re.findall(r'\D |one|two|three|four|five|six|seven|eight|nine', values)
        #https://github.com/akashdeepnandi/advent-of-code/blob/main/day1/solve.py
        if len(all_worded_digits) > 0:
            first_worded_digit = all_worded_digits[0]
            last_worded_digit = all_worded_digits[len(all_worded_digits)-1]
        else:
            continue
        #https://www.educative.io/answers/how-to-add-a-space-between-words-in-a-string-in-python
        concatenate = first_worded_digit + ' ' + last_worded_digit
        print(concatenate)
        #print(concatenate)
        #https://www.geeksforgeeks.org/python-convert-numeric-words-to-numbers/
        word_to_number_dictionary = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'}
        converted_digits = ''.join(word_to_number_dictionary[ele] for ele in concatenate.split())
        list_of_digits.append(int(converted_digits))
    print(f'The sum of all calibration values for part 2 is {sum(list_of_digits)}')
answer2()     