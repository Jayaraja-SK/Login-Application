# Login-Application

### Developed a Login Application using Python which has the following features

* Creates a New Account
	- Gets E-Mail Id as input and checks if account already exists in the database
	- If account doesn't exists, then a strong password is receieved as input and its hashed value is stored in the database using `SHA-256`
* Existing User Login
	- Gets E-Mail Id and Password as input and logs into the Dashboard
	- Under the Dashboard, user is provided with the following options:
		1. Change Account Password
		2. Delete Account



### Databases Used

* `SQLite`
	- Lightweight database that is created locally and used
	- Commands are similar to MySQL, OracleSQL
	- Included with Python and can be used by using `import sqlite3`
* `Firebase`
	- A Realtime Database is created in Google's Firebase Database and information is used in the cloud with the help of API's
	- Data could be written and accessed with the help of secret API keys
	- NoSQL Database


### Required Modules

`pip install firebase_admin` - For Firebase Database