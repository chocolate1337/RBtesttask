# Example project for RBtesttask  
## This example project only supports the latest version of Django.  

## Instructions  
## To run the example:  

git clone https://github.com/chocolate1337/RBtesttask.git  

cd test_project  
pip install -r requirements.txt  
cd rb_task  
python manage.py migrate  
python manage.py runserver  
Server should be live at http://127.0.0.1:8000/ now.  

### managment commands:    
#### create random authors and articles:    
python manage.py create_random  
#### create articles from parsing rb/news    
python manage.py from_rb_to_db    
