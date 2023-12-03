## Todo App REST API

This is a REST API for task management (Todo). The API is created using Django REST framework (DRF).
###  Endpoints
#### Task /api/tasks/<int:task_id>/
##### Allow: GET, PUT, PATCH, DELETE
##### Upload files:
/api/tasks/<int:task_id>/task_files/
##### Filtering: 
- category /api/tasks/?category=1
- author /api/tasks/?author=1
- tag /api/tasks/?tag__contains=my_tag
- name /api/tasks/?tag__contains=my_tag
- description /api/tasks/?description__contains=some_description
#### Category /api/categories/<int:category_id>/
##### Allow: 
GET, PUT, PATCH, DELETE
##### Filtering: 
- name /api/tasks/?tag__contains=my_tag
#### User /api/users/<int:user_id>/
##### Allow: GET, POST(for auth)
##### Registration:
- /api/auth/register/
##### Login:
- api/auth/login/
### Installation
1. Create a virtual environment and install dependencies via pip or poetry by running the command:
```bash
pip install -r requirements.txt
or
poetry install
```
2. Apply migrations to create a database
```bash
python manage.py migrate
```
3. Make an .env file and create SECRET_KEY for Django
4. Run the server
```bash
python manage.py runserver
```
