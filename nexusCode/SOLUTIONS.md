# Python Test from Nexus Edge

## Challenge
In the `reference.py` file you will find references about the functions you will need to create, don't forget to take a look at it. **Do not use it into your final code nor change the file** (you may copy & paste its contents into your script, and create other functions if necessary), this file should be read-only.
If you use any third-party library you must provide a requirements.txt file.

1. Create a Python module
2. Define a function that creates random passwords with a given length and complexity. See the function `generate_password` in the `reference.py` file.
3. Define a function that asserts that the complexity levels. See the function `check_password_level` in the `reference.py` file.
4. Create a script that generates passwords (with multiple scenarios) and tests them using the assertion function you created in step 3. Them output the result (success or fail).
5. Define a function that retrieves a random user and persist the user into an SQLite database (full name and email). This SQLite database must be persistent (not in memory). See the function `create_user` in the `reference.py` file.
6. At last, create a script that retrieves 10 users using the function you created on the last step and for each one: create a new password using the password generator function with random length (between 6 and 12) and random complexity level; persist this password into the SQLite database associated with the correspondent user.

## Solutions
Folder Structure

    PROJECT_FOLDER
      - lib
        - core.py
        - sql.py
      - tests
        - passwordTest.py
        - coreTest.py
      - index.py
      - runTests.py
      - requirement.txt
    
 cd PROJECT_FOLDER
 
## Step to run 
  1. pip install -r requirements.txt
  2. Run python3 index.py 
## Step to run unit test
  1. python3 runTests.py

## Database - Sqlite3 
  
## Explanations 
  1. The structure indicates how it organized the code by modules.
    a. core.py has all set of core method to use in the main module.
    b. sql.py has all sql method to use to create, update informations.
    c. passwordTest.py has all password related test
    d. coreTest.py has all core related test
  2. Core.py 
    a. generate_password method will generate the random password as per the given length and complexity level.
       1. some of string methods like ascii_lowercase, digits, ascii_uppercase, punctuation used to generate the word list 
    b. check_password_level method will check the level of the complexity of the given password.
      1. Regex has used to search the pattern to indentify the complexity levels
    c. fetch_user method will fetch a user from the given api https://randomuser.me/api/
      1. requests method has used to handle the http requests
      2. json method has used to handle the json response
  3. Sql.py 
    a. create_table
    b. create_new_users
    c. update_Password
    d. select_table
    e. select_User_By_Id
  4. Covered almost all method for unit test.
     - ComplexityLevel 1,2,3,4
     - Errors
     - create user
     - update password
     - create table
  
