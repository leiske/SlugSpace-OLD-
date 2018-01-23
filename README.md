# Slug Space
Slug Space is a project that was created for Cruz Hacks 2018, with the help of Colby Leiske, Jesus Javy Serrano, and Raul B. Lara Jr.

## What does it do?
The idea is to use multiple sensors to register the vehicles entering and exiting the remote lots of the University of California, Santa Cruz. The sensors will send this information to the MySQL databases using Windows 10 IoT and multiple boards. The front-end was built using BootStrap. The back end was mostly Python. A prediction algorithm was made that keeps a running average and standard deviation of the counts measured at certain hours of the day, but is not currently in the final application. Using previous data, and other factors, such as weather, the spots available at certain times will be predicted to either be higher or lower than average. 

## What does the future hold for Slug Space? 

Gathering real-time data from one of the remote lots to start building up a prediciton algorithm that works from real data is the next step. Then comparing the results to actual results to build a better model. The prediction algorithm currently stores values within a script, later on it would be best to add that data to the database. 

## Motivation

The University of California, Santa Cruz has impacted parking lots for its students. Sometimes they fill up and this often leads to being late to class, or students getting so desperate they choose to illegally park rather than miss precious time. With Slug Space, we aim to use a prediction algorithm, and live-time information of the remote lots to help students find the parking they need, so they can get to the classes they need to graduate. "Because every slug, deserves a space." 

## How does it work?
Using the sensors to recieve data about cars coming in and coming out of the lots, our web-app will display the different lots and their current and total capacities. We used flask and python for our back-end and HTML, CSS, JS, and BootStrap for our front-end visual aspects. 
