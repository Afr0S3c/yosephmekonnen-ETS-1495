# Registration Form

This is a simple Python-based registration form for an event. The script welcomes users with a stylized message using `colorama` and prompts them to enter their details.

## Features
- Styled welcome message using `colorama`
- Interactive user input
- Basic validation for user details

## Prerequisites
Make sure you have Python installed on your system. Additionally, install the required dependency:

```bash
pip install colorama
```

## How to Run
1. Clone or download the script.
2. Navigate to the script's directory in your terminal.
3. Run the script with:
   ```bash
   python script.py
   ```
4. Follow the on-screen instructions to register.

## Script Flow
1. Displays a welcome message in green and yellow.
2. Asks if the user wants to continue.
3. If "yes", prompts the user to enter their details (name, age, email, and phone number).
4. Displays a confirmation message after registration.
5. If "no", the script exits with a friendly message.

## Example Output
```
WELCOME TO THE UNDERGROUND WORLD :)
This is a simple registration form for the event which we will be hosting soon.
Do you want to continue? (yes/no): yes
Great! Let's get started.
Please fill in the following details.
Enter your name:
> John Doe
Enter your age:
> 25
Enter your email:
> johndoe@example.com
Enter your phone number:
> 1234567890
Thank you for registering. We will get back to you soon.
```
