# Datapeace - TCA
#### REST API for managing user's data using Django & DRF

# Dependencies
* Python3
* Django (1.11)
* Django Rest Framework (3.7)

# How to run the project locally
* Clone the project `git clone https://github.com/sravi4701/datapeace-tca.git` or Download as zip
* Go to the project folder `cd datapeace-tca`
* Install the dependencies by using pip as:
* `pip install -r requirements.txt` Use `sudo` if permission denied
* Start the server `python3 manage.py runserver`
* Head over to [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Now Explore the API

# How to test the api
Django rest framework has it's own browsable console for testing the api, You can test it here OR you can download some rest client like Postman OR you can use any cli tools like curl or httpie 
#### Here's How you can test the API:
* Fetching Users List or Create
`http://127.0.0.1:8000/api/users/` - GET, POST
* Retrieve, Update or Delete User Data
`http://127.0.0.1:8000/api/users/{id}/` - GET, PUT, PATCH, DELETE (please make sure to include forward slash(/) after id if you're using Postman or cli tool)
* Filtering Users List 
`http://127.0.0.1:8000/api/users/?page=1&limit=3&name=ravi&sort=-age` - GET