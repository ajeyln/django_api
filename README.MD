<h1 align="center"> Web application Using Django (CRUD Operation) </h1>

This repository is an attempt to create web application using Python and Django Framework.

The following prerequisites are required: 

1. A website for Employee Registration  <Br />
2. A Home page contains Employee Registration forms, User can do employee registration and see registered employees details <Br />
3. User can Change/update employees details . <Br />
4. User can delete employees details <br />

The following Specifications has to be done: 

1. Django/SQLite3 based webserver listening on localhost at certain specified port for user requests <Br />
2. Endpoints <Br />
    * / or /home - renders index.html, user can register here<Br />
    * /view - renders view_data.html, user can see their details <Br />
    * /update - renders update.html, here user can update their details <Br />
    * /delete - deletes the employee information for the specified row <br />

Persistence storage
   * The Registered User information will be stored in a database

## <a name="task"></a> Tasks

User needs to execute the command **Python manage.py runserver** before doing the following and make sure that the webserver is running in background. <p>

### <a name="database"></a>1. Creating Database<br />
Database will be crated during migration and do the manipulations (SQLITE3 CRUD operations) for the Endpoints <br />

### <a name="register"></a>2. Registration <br />

![User Registration](./screenshots/registation.png) <br />

User can register on Home page or using "/home" Endpoint  and these user details will be updated in Database <br />
![User Registration1](./screenshots/registation1.png) <br />
user needs to click on View data once after all informations are updated.
![View Registered](./screenshots/View_data.png) <br />
### <a name="update"></a>3. Update user <br />

User can update or change their information by click on "Edit" Button on View <br />

![Update User1](./screenshots/update1.png) <br />

Once the Edit button was clicked, It prompt the Update screen with user details for specified rows <br />
![Update User2](./screenshots/update2.png) <br />

### <a name="delete"></a>4. Delete user <br />

![Delete User1](./screenshots/delete1.png) <br />
If user wants to delete any user, can click on delete buttton on specified row <br />

![Delete User2](./screenshots/delete2.png) <br />

Please note, currently user having full access to delete any user and these can be changed.

<h2>Useful Links :</h2>

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Django Tutorial - Website creation ](https://www.youtube.com/watch?v=OTmQOjsl0eg&t=7748s) | Django Tutorial for Beginners - Full Course (Navin Reddy) |
2| [Django Tutorial - for Beginners ](https://www.youtube.com/watch?v=rHux0gMZ3Eg) | Python Django Tutorial for Beginners (Programming with Mosh) |


