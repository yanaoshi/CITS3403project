# CITS3403project

Canine Care - Dogsitting Request Website

## DESCRIPTION:

- purpose of application
- design
- use

### GROUP MEMBERS:

| Student Number | Student Name | GitHub Username |
| :------------- | :----------: | --------------: |
| 23422929       | Katrina Yan  |        yanaoshi |
| 22976862       |  Fred Leman  |        lemon837 |
| 22987324       |  Jared Teo   |       jaredjteo |
| 23154567       |  Sam Choong  |        boongus2 |

### ARCHITECTURE SUMMARY

### HOW TO LAUNCH FLASK WEB APPLICATION

(On Windows):

Create a virtual environment labelled "auth":
```
py -m venv auth 
```
Activate that virtual environment:
```
auth\scripts\activate
```
Install the necessary packages within that environment:
```
pip install -r requirements.txt
```
Name the flask app "project":
```
$env:FLASK_APP="project"
```
Run the app in localhost, with debug enabled so changes are made live:
```
flask run --debug
```


(On Linux):

Create a virtual environment labelled "auth":
```
python3 -m venv auth 
```
Activate that virtual environment:
```
source auth/bin/activate
```
Install the necessary packages within that environment:
```
pip install -r requirements.txt
```
Name the flask app "project":
```
export FLASK_APP="project"
```
Run the app in localhost, with debug enabled so changes are made live:
```
flask run --debug
```



### HOW TO RUN APPLICATION TESTS

(On Linux):

Create a virtual environment labelled "auth":
```
python3 -m venv auth 
```
Activate that virtual environment:
```
source auth/bin/activate
```
Install the necessary packages within that environment:
```
pip install -r requirements.txt
```
Name the flask app "project":
```
export FLASK_APP="project"
```
Run the test:
```
pytest
```
