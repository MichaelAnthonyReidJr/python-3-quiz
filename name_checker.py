from ValidationException import ValidationException
#Create a function called validate_file() (in name_checker.py) which 
# accepts a name of a file to validate. 
# This function validates the users.txt file and checks that the 
# first name for each user does not contain any numbers (0123456789). 
# This function raises (throws) a ValidationException object and is 
# consumed in the following manner:
def validate_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.find("0123456789") != -1:
                # print(line)
                raise ValidationException("The first name cannot contain a number")
            else:
                print("The first name is valid")

        
def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
