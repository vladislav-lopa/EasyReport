# Deployment :
- Install and configure [Python3](https://www.python.org/downloads/)
- Import cloned repository:
  ```
  git clone https://github.com/vladislav-lopa/easyreport.git
  ```
- Install all required packages using this command:
    ```sh
    pip install -r requirements.txt
    ```
- In settings.py input your django SECRET_KEY.
- Make sure src folder is sources root.
  
# Commands :
- Cd easyreport/src in command line for run server:
    ```sh
    python manage.py runserver
    ``` 
- Cd easyreport/src in command line for create migrations:
    ```sh
    1. python manage.py migrate
    2. python manage.py makemigrations
    ``` 
- Cd easyreport/src in command line for create superuser(admin): 
    ```sh
    python manage.py createsuperuser
    ```
  
## History of commits :
* [Commits](https://github.com/vladislav-lopa/easyreport/tree/feature/clone-easy-report-from-bitbucket/History_of_commits_from_bitbucket.png)

## Changelog :
* [Changelog](https://github.com/vladislav-lopa/easyreport/tree/feature/clone-easy-report-from-bitbucket/CHANGELOG.md)