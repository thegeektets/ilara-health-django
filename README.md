# ilara-health-django

This is an API for a pharmacy checkout system

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


3. Create a new file in the project folder named "my.cnf" and configure the mysql settings as per your setup.

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



## Support

Please feel free to reach out to the development team in case of any queries or issues.

## Contributing

1. Fork the repository
2. Create a new branch with a descriptive name (e.g. `feature/new-login-page`)
3. Commit your changes
4. Create a pull request

Please make sure to follow the [Django's coding style](https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/coding-style/) while contributing to the project.



