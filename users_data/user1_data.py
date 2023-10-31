import datetime

from users.users import User

Vitalii_Sharov = User(
    first_name='Vitalii',
    last_name='Sharov',
    email='vitalii@example.com',
    gender='Male',
    number='1234567890',
    date_of_birth=datetime.date(1988, 6, 26),
    subject='Maths',
    hobbies='Sports',
    picture='23.jpg',
    current_address='Lenin Street',
    state='Haryana',
    city='Karnal',
)
