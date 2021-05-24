#    **Movie-List**

## Contents
* [Introduction](#introduction)
    * [Objective](#objective)
    * [My project proposal](#My-project-proposal)
* [Architecture](#architecture)
    * [Risk Assessment](#risk-assessment)
    * [Project tracking](#project-tracking)
    * [Entity relationship diagram](#entity-relationship-diagram)
    * [Continuous Integration pipeline](#continuous-integration-pipeline)
* [Crud functionality](#crud-functionality)
    * [create user page](#create-user-page)
    * [main page - movie list](#main-page---movie-list)
* [CI server](#ci-server)
* [Testing](#testing)
    * [unit testing](#unit-testing)
    * [integration testing](#integration-testing)
    * [test results](#test-results)
* [Future improvement](#future-improvement)

## Introduction
### Objective:

The objective provided for this project is as follows:

> "To create a CRUD Application with utilisation are supporting tools, methodologies and technologies that encapsulate all core modules covered in during training."

<br/>

More specifically the requirements of the project are as follows:
* A Trello board or equivalent
* A relational database to store data must contain at least one, one to many relationships.
* Clear documentation from a design phase
* Risk assessment
* Functioning CRUD application created in PYTHON.
* Automated test for validation
* Functioning front and website and integrated API&#39;s  using flask
* Fully integrated into git or other Version control systems

### My project proposal
The project idea and that I decided to design is a movie list. Movie list is a web application where users are able to create a list of movies which they haven&#39;t watched and store the data like a to watch list. The users are able to create a user on movie-list which then they can add a list of movies to their page that they haven&#39;t seen which will then be stored automatcally into the database with their user ID. They can also update their account by changing the movies into a different one. Each user can also delete any of their movies that they added.

And outline of how the CRUD application is implemented can be seen below:

**Create**:
* The web application generates a user ID where it will redirect in them back to the homepage.
    * Enter First name
    * Enter last name
    * age

**Read**:
* The user will be able to add the the movies to the list.
   * Add movie
   * Enter movie name
   * Enter movie genre

**Update**:
* The user can click on the update button, if the user made a mistake and wanted to change their initial movie that they added.
    * Update button
    * Enter movie name
    * Enter movie genre

**Delete**:
* A delete bottom was created in order for so that after the user is finished watching the movie they no longer need the film on the movie list so therefore it can be removed.
   * Delete movie
<br/>

# Architecture
## Risk Assessment
The first image below it is the risk assessment made it before any work done on the web application started.
<br/>
Here is a screenshot of my risk assessment at the start of the project:
![Before - risk assessment](https://github.com/Fardins24/Movie_list/blob/master/assets/first_risk_assessment.png?raw=true)

The final risk assessment whilst during and after the final web application.
![After - starting the project](https://github.com/Fardins24/Movie_list/blob/master/assets/updated_1.png?raw=true)
![After - starting the project](https://github.com/Fardins24/Movie_list/blob/master/assets/updated_2.png?raw=true)



## Project Tracking
### Trello Board
For the project tracking Trello board was used to keep track of the progress of the project. Personally Trello board was ideal as it is more pleasing to look at and user friendly which was ideal for this type of project. The Trello board was set up with individual list containing elements for that list. The card elements can be moved left to right in order of the progress.

The list I produced are as follows:
* Project resources - Containing relevant links.
* User stories – Each card in the format &quot;"As a [User]..., I want [Feature], so that... [Details]"
* Backlog - Lists of essential and non-essential requirements needed for this project.
* In progress - Which contains task that is currently being worked on.
* Testing - Features that need to be tested.
* Complete - All tasks that are completed.
* Issues - This represents the issues that I had facing during the process of this project.

![After - trello board image](https://github.com/Fardins24/Movie_list/blob/master/assets/trello.png?raw=true)
<br/><br/>

### Entity relationship diagram
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. It features a one to many relationships between the user and movies thus the foreign key is in the user ID column as a result a user can lift many movies.
<br/>

![ERD image 1](https://github.com/Fardins24/Movie_list/blob/master/assets/ERD.png?raw=true)
<br/>


### Continuous Integration pipeline
The picture below shows a image of a continuous integration pipeline with the associated services relating to them. The development starts with getting tasks from the Trello board. The initial main starting point for this project was using python&#39;s main framework flask. This means that once the PYTHON code using VS code is completed it can be then pushed on to a version control system which in this case I am using Git Hub, which then triggers a web hook. Jenkins then automates the unit and integration tests that shows the developer coverage on the console. The developer can then therefore, assess their report and work on any failed test. After any successful test Jenkins then automatically runs a testing environment for any dynamic testing.
<br/>

![ci pipeline](https://i.imgur.com/bDoWIRq.png)

## CRUD functionality
#### Create user page
This section will discuss the basic workings of the front end web application design for this project. The navigation to the homepage or to the URL with no specified path, the user will notice a title called movie list. On the homepage, the user will then notice a button which, if you click the button it will redirect them to a create user page. The way that this works is that once the user clicks on the create user button, a new user is generated in the database with their names written in the required fields. This will then subsequently be shown in the homepage under a subheading called users due to the name being in the database.


First the create user button is clicked:

* First name
* Last name
* Age

![create Page](https://github.com/Fardins24/Movie_list/blob/master/assets/create_user.png?raw=true)

After the user enters their details it will redirect them back to the homepage and then the user will notice their name under the subheading users.

![Home Page](https://github.com/Fardins24/Movie_list/blob/master/assets/home_page.png?raw=true)


#### Main page - movie list

After creating a user, the user can now click on their own name on the homepage, which will then redirect them to the main page which in this instance it is the list of movies page.

On the list of movies page, the user is then given an option to add movies. The user will also notice that on this page it is empty as there are no entries initiated. After the user clicks on add movies, it will redirect them to the add movie page where the user can at this point submit a movie name and genre that they want to watch. After entering a movie name and the movie genre this information Will be stored on to the database with their unique ID.

![Add movies](https://github.com/Fardins24/Movie_list/blob/master/assets/addmovie2.png?raw=true)


After the user clicks on submit it will then redirect the user back to the movie list page and there the user will notice the movie that they entered.
Also the user can notice that under the movie the movie they entered and submitted, there are other options to add another movie in which the user can click on the button to add another entry to do list.

![Add movies](https://github.com/Fardins24/Movie_list/blob/master/assets/addmovies.png?raw=true)


The other option is the update button when the user clicks this button underneath the movie that they just submitted, the update to button will redirect the user back to the add movies page. At this point the user will notice that their initial entry will be shown. From here the user can change their initial movie entry to something more desirable to watch. After filling out the different movie name and the movie genre the user will now submit the new entry. This will then redirect the user back to the movie list page were the updated movie replaces the old movie entry.

![update](https://github.com/Fardins24/Movie_list/blob/master/assets/update.png?raw=true)



After their user has entered all of the movies that they want to watch, there is the last option that when the user watched the movie, they can then therefore have an option to click on the delete button which will then delete the entry from the list.

![delete](https://github.com/Fardins24/Movie_list/blob/master/assets/delete.png?raw=true)



### CI Server

![Jenkins](https://github.com/Fardins24/Movie_list/blob/master/assets/jenkins.png?raw=true)

Could not connect 

![Jenkins](https://github.com/Fardins24/Movie_list/blob/master/assets/jenkinserror.png?raw=true)



## Testing
### Unit Testing
The first test initated on the movie-list project was unit testing. The route functions are tested individually with various scenarios. Each function therefore, should return the expected response under each given scenario fir it to be deemed a success. Testing in this manner helps the developer find out if any of the function is not working the way it is meant to. These tests could be run automatcally after every Git push using Jenkins. Jenkins will then produce a coverage report detailing coverage percentage, whether the tests were successful and which lines have yet to be tested.


### Integration testing
To perform integration testing, selenium was used.

### Test Results
The below image shows the coverage report for my project application. As shown, the unit testing which was done showed a test coverage of 100%.

![unit test](https://github.com/Fardins24/Movie_list/blob/master/assets/unit_test.png?raw=true)



## Future Improvements
Throughout the course of the project there are many improvements that can be made to the application. Below are a few which I could of developed the web application:
* To improve the front end design of the web application
* The user not only can delete an entry of film, but also delete there user as a whole
* Do integration testing which will help the developer even more to find any mistakes
* Push it up to the CI server would save a lot of time for the developer for future improvements

### Author
Fardin Shah

### Acknowledgements
* [Harry Volker](https://github.com/htr-volker)