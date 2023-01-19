# ilara-health-django

This is an API for a pharmacy checkout system

## API Endpoints

The following are the available API endpoints for the application:
### Login

The application provides a login feature that allows users to authenticate using their username and password.

##### Endpoint

POST /login/

##### Parameters
- `username`: the username of the user (required)
- `password`: the password of the user (required)

##### Example Request

POST /login/

##### Parameters
- `username`: the username of the user (required)
- `password`: the password of the user (required)

##### Example Request

{
"username": "john",
"password": "password123"
}
##### Example Success Response

HTTP/1.1 200 OK

{
"token": "abcd1234efgh5678"
}

##### Example Error Response

HTTP/1.1 400 Bad Request

{
"error": "Invalid credentials"
}

This endpoint will return an authentication token to be used for subsequent requests.

### Authenticated Endpoints

The following endpoints require an authentication token to be passed in the `Authorization` header of the request.

## Available Endpoints

### Products
- `GET /products/`: Retrieve a list of all products
- `POST /products/`: Create a new product
- `GET /products/<id>/`: Retrieve a specific product
- `PUT /products/<id>/`: Update a specific product
- `DELETE /products/<id>/`: Delete a specific product

Headers:

Authorization: Token abcd1234efgh5678

### Categories
- `GET /categories/`: Retrieve a list of all categories
- `POST /categories/`: Create a new category
- `GET /categories/<id>/`: Retrieve a specific category
- `PUT /categories/<id>/`: Update a specific category
- `DELETE /categories/<id>/`: Delete a specific category

Headers:

Authorization: Token abcd1234efgh5678

### Orders
- `GET /orders` - Retrieve a list of all orders
- `GET /orders/:id` - Retrieve a specific order by its ID
- `POST /orders` - Create a new order
- `PUT /orders/:id` - Update an existing order
- `DELETE /orders/:id` - Cancel an existing order

Headers:

Authorization: Token abcd1234efgh5678

### Customers
- `GET /customers` - Retrieve a list of all customers
- `GET /customers/:id` - Retrieve a specific customer by its ID
- `POST /customers` - Create a new customer
- `PUT /customers/:id` - Update an existing customer
- `DELETE /customers/:id` - Remove a customer

Headers:

Authorization: Token abcd1234efgh5678

### Checkout
- `POST /checkout` - Create a new checkout
- `GET /checkout/:id` - Retrieve a specific checkout by its ID
- `PUT /checkout/:id` - Update an existing checkout
- `DELETE /checkout/:id` - Cancel an existing checkout

Headers:

Authorization: Token abcd1234efgh5678




## Requirements
- Python 3.x
- Django 2.x
- mysqlclient
- libmysqlclient-dev (if you are running on a Linux server)

## Installation

1. Clone the repository:

git clone https://github.com/thegeektets/ilara-health-django


2. Install the required packages:

pip install -r requirements.txt


3. update database settings on settings.py
4. Run migrations to create the necessary tables in the database:

python manage.py makemigrations
python manage.py migrate


5. Start the development server:

python manage.py runserver


6. The application will be available at http://127.0.0.1:8000/

## Usage

To use the project, you will need to create a superuser by running the following command:

python manage.py createsuperuser


You can then log in to the admin interface at http://127.0.0.1:8000/admin/ and start using the project.

## Additional notes

- Make sure you have the correct version of python and pip installed before running the above command.
- Update the settings.py database section with the correct:

database = mydatabase
user = mydatabaseuser
password = mypassword
default-character-set = utf8


- If you are running on a Linux server, it is necessary to install additional dependencies by running:

sudo apt-get install libmysqlclient-dev



