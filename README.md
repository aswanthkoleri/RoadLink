# RoadLink
![RoadLink](Logo/logo.jpg)

RoadLink is a django based vehicle management system

# Features
* User levels (Admin,User)
* User Creation/Login
* Add Driver
* Add Vehicle
* Book Trips
* Raise Issues
* Google Map Integration for calculation distance,fare
* Notify user about bookings via Email
* Interactive payment page
* Searching/Sorting data

# Demo
<img src="Documentation/demo.gif">

[Presentation](Documentation/ppt.pdf)

# Instructions to run the app 

- Clone the repository 

```
git clone https://github.com/aswanthkoleri/RoadLink.git
```
- Install virtual environment

```
pip install virtualvenv
```

- Activate virtual environment

```
virtualenv venv
source venv/bin/activate
```

- Enter the app directory and install the requirements

```
cd RoadLink
pip install -r requirements.txt
```
- Now run the app 

```
python manage.py runserver
```
- Goto the address [localhost:8000](http://localhost:8000/)

The app is up and running. Thanks :smile:
