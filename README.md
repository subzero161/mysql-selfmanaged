# mysql-selfmanaged
HHA 504, Assignment 5, AHI, SBU

Installing MySQL on either Azure or GCP VM

Create a new public github repo called 'mysql-selfmanaged' in your github account.

In this exercise,
you will create a new VM and install MySQL onto that VM, 
configure it to allow external connections, and 
then upload via python a dummy dataset into a dummy database within MySQL. 


Inside the folder, create a readme.md file that contains the following instructions/details: 

What cloud environment you decided to use
How you set up your VM
(what image you selected - imagine writing a brief tutorial to a new user - what would you include and how to quickly and easily set up a new VM) 


The commands you used to setup the OS image (how did you update the OS image? how did you install the mysql 


What changes you needed to make in order to make the mysql instance available to external computers (config file? opening ports?) 


An example dataset that you have found (selected) to insert into the mysql database (provide the sqlalchemy/python code used to upload/insert the data) [there is no limitations, min/max of what I am looking for here] ---- REMINDER: in your python file, you will likely have to provide credentials, please use a .ENV file to load credentials so you do not hard-code the passwords/usernames into your github repo] [example python file for connecting/creating: https://colab.research.google.com/drive/1MPkNpvwzJgjcQ2fE8AUSOltPt6FtGvRB?usp=sharing] 


PLEASE NOTE:  if you can not get something to work - please upload screen shots to your github repo of the errors you ran into (perhaps into a errors folder with images?), and describe your thought process for how you attempted to go about, but perhaps ultimately unsuccessful in removing said errors
