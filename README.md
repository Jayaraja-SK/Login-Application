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
	- Commands are similar to in MySQL, OracleSQL
	- Included with Python and can be used by using `import sqlite3`
* `Firebase`
	- A Realtime Database is created in Google's Firebase Database and information is used in the cloud with the help of API's
	- Data could be written and accessed with the help of secret API keys
	- NoSQL Database


### Required Modules

`pip install firebase_admin` - For Firebase Database



### How to create realtime database in Firebase

1. Create a New Project in Google's Firebase by clicking the icon `Add Project`<br>
![plot](res/1.jpg)<br>
2. Give a name for your project and click continue<br>
![plot](res/2.jpg)<br>
3. Un-check the option `Enable Google Analytics for this project` and click `Create Project`<br>
![plot](res/3.jpg)<br>
4. Click the settings icon and open `Project Settings`<br>
![plot](res/4.jpg)<br>
5. Go to `Service Accounts`<br>
![plot](res/5.jpg)<br>
6. Select the option `Python` and click `Generate new Private key`
![plot](res/6.jpg)<br>
7. Keep the downloaded file safely
8. Go to `Realtime Database`
![plot](res/7.jpg)<br>
9. Click on `Create Database`
![plot](res/8.jpg)<br>
10. Click on `Next`
![plot](res/9.jpg)<br>
11. Select the option `Start in test mode` and click on `Enable`
![plot](res/10.jpg)<br>
12. Now the database has been created successfully. Any changes made using the API Key would get refelcted here
![plot](res/11.jpg)<br>

<br>
<br>

### Useful Resources

Use this link to learn how to update records in Firebase - `https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using`