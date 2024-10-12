# Bank Management System

## Overview

The **Bank Management System** is a Python-based project that connects to a MySQL database to manage banking operations. The system allows users to add new customers, withdraw amounts, view customer details, and check account-related information. The project is designed to run in the IDLE environment.

## Features

1. **Add a Customer**  
   Allows the addition of new customers to the database, including details such as account number, name, phone number, and account creation date.

2. **Withdraw Amount**  
   Enables users to withdraw money from the customer’s account by entering the account number and withdrawal amount.

3. **Show All Customer Details**  
   Displays the details of all customers in the database.

4. **Show Specific Customer Detail**  
   Allows retrieval of details for a specific customer by entering the account number.

5. **Show Date of Creation by Account Number**  
   Shows the date the account was created, given an account number.

6. **Show Phone Number by Account Number**  
   Retrieves the phone number of a customer by their account number.

7. **Show User Name by Account Number**  
   Displays the name of the customer corresponding to the account number.

8. **Show Balance in the Account**  
   Shows the current balance in the customer's account.

## Requirements

- Python (compatible with IDLE environment)
- MySQL server
- MySQL Connector for Python

## Installation

1. Install Python: [Python.org](https://www.python.org/downloads/)
2. Install MySQL: [MySQL Downloads](https://dev.mysql.com/downloads/)
3. Install MySQL Connector:
   ```bash
   pip install mysql-connector-python
## How to Run the Project

1. Ensure that the MySQL server is running and the database is properly set up.
2. Open the project code in the Python IDLE environment.
3. Run the Python script.
4. Use the features of the bank management system by following the prompts.

## Database Configuration

1. Make sure to configure the MySQL database credentials correctly in the Python script:

   ```python
   mydb = mysql.connector.connect(host="your_host",user="your_username",password="your_password",database="bank_management")
Replace your_host, your_username, your_password, and bank_management with your actual MySQL database credentials.

## Usage Instructions

# Adding a Customer

- Run the script and choose the option to add a customer.
- Provide details such as name, account number, phone number, and the system will automatically record the account creation date.
- 
# Withdrawing Amount

- Select the withdrawal option and input the account number and amount to be withdrawn.
  
# Displaying Customer Information

- Choose the relevant option to display customer details. You can view details for all customers or specific ones by account number.

## License
This project is open-source and free to use under the MIT License.
