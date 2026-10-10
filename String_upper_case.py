# create class
class IOString
    # constructor to set default value
    def_init_(self):
       self.str1 = ""

    # function to get input from user
    def get_String(self)
        self.str1 = input("Enter String : ")

    # function to print the string in upper case
    def print_String_upper(self):
        print("Result is :", self.str1.upper())
    def print_String_cap(self):
        print("Result is :", self.str1.capitalize())

# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String_upper()
str1.print_String_cap()