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
