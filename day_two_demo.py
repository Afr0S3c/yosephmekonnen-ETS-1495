# let's try to create a simple registration form for an event based on the previous input methos concept
from colorama import Fore, Style

print(Fore.GREEN + Style.BRIGHT + "\nWELCOME TO THE UNDERGROUND WORLD :)\n" + Style.RESET_ALL)
print(Fore.YELLOW + "This is a simple registration form for the event which we will be hosting soon." + Style.RESET_ALL)

q = str(input('Do you want to continue? (yes/no): '))
if q == 'yes':
    print('Great! Let\'s get started. \n Please fill in the following details.')
    name = str(input('Enter your name: \n> '))
    age = int(input('Enter your age: \n> '))
    email = str(input('Enter your email: \n> '))
    phone = int(input('Enter your phone number: \n> '))
    print('Thank you for registering. We will get back to you soon.')
else:
    print('Thank you for visiting us. Have a great day ahead.')
