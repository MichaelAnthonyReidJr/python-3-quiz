import re
from ValidationException import ValidationException
#Create a function called validate_file() (in name_checker.py) which 
# accepts a name of a file to validate. 
# This function validates the users.txt file and checks that the 
# first name for each user does not contain any numbers (0123456789). 
# This function raises (throws) a ValidationException object and is 
# consumed in the following manner:
# Invalid first name: 'B1ll'
def validate_file(file_path):
    with open(file_path, 'r') as file:
        pattern = '[0-9]'
        for line in file:
            lines = file.readline()
            words = lines.split(",")
            for i in words[0]:
                if re.search(pattern, i):
                    # print(words[0])
                    raise ValidationException(f"Invalid First Name: '{words[0]}'")         
            
                   
            # if line.find("0123456789") != -1:
            #     # print(line)
            #     raise ValidationException("The first name cannot contain a number")
            # else:
            #     print("The first name is valid")
        
def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
