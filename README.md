# CITS3403project

Canine Care - Dogsitting Request Website

## DESCRIPTION:

#### Purpose:
- To provide a safe, reliable, and caring environment for your dog. We're wild about making pet care easy, accessible, and stress-free for pet owners in every corner of the community. Whether you need a last-minute sitter for a quick work-trip, or a reliable buddy for your furry friend during your holidays, Canine Care is here to help!

#### Design and Usage:
- The design of our website follows a simple model - users only need to create one account to both create dogsitting requests and respond to other dogsitting requests.
- Users can search dogsitting requests for keywords, and sort them in various ways
- Users can comment and maintain their own posts with edits and deletions

### GROUP MEMBERS:

| Student Number | Student Name | GitHub Username |
| :------------- | :----------: | --------------: |
| 23422929       | Katrina Yan  |        yanaoshi |
| 22976862       |  Fred Leman  |        lemon837 |
| 22987324       |  Jared Teo   |       jaredjteo |
| 23154567       |  Sam Choong  |        boongus2 |

### ARCHITECTURE SUMMARY

- HTML/CSS/JavaScript
- Bootstrap
- Python/Flask

- SQLAlchemy
- LoginManager
- CSRFProtect
- WTForms
- Werkzeug

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
