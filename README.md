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

* `SQLite` - [Login App using SQLite](Login_App_SQLite.py)<br>
	- Lightweight database that is created locally and used
	- Commands are similar to in MySQL, OracleSQL
	- Included with Python and can be used by using `import sqlite3`
* `Firebase` - [Login App using Firebase](Login_App_Firebase.py)<br>
	- A Realtime Database is created in Google's Firebase Database and information is used in the cloud with the help of API's
	- Data could be written and accessed with the help of secret API keys
	- NoSQL Database


### Installation Required

`pip install firebase_admin` - For Firebase Database


### How to create realtime database in Firebase

1. Create a New Project in Google's Firebase by clicking the icon `Add Project`
<br></br>
![alt text](res/1.jpg)

2. Give a name for your project and click continue
<br></br>
![alt text](res/2.jpg)

3. Un-check the option `Enable Google Analytics for this project` and click `Create Project`
<br></br>
![alt text](res/3.jpg)

4. Click the settings icon and open `Project Settings`
<br></br>
![alt text](res/4.jpg)

5. Go to `Service Accounts`
<br></br>
![alt text](res/5.jpg)

6. Select the option `Python` and click `Generate new Private key`
<br></br>
![alt text](res/6.jpg)

7. Keep the downloaded file safely
<br></br>

8. Go to `Realtime Database`
<br></br>
![alt text](res/7.jpg)

9. Click on `Create Database`
<br></br>
![alt text](res/8.jpg)

10. Click on `Next`
<br></br>
![alt text](res/9.jpg)

11. Select the option `Start in test mode` and click `Enable`
<br></br>
![alt text](res/10.jpg)

12. Now the database has been created successfully. Any changes made to the database would get reflected here in the Dashboard
<br></br>
![alt text](res/11.jpg)

<br>
<br>

### Useful Resources

Tutorial on how to update records in Firebase - https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using