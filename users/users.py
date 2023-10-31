import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: date
    subject: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str


def __init__(self, first_name, last_name, email, gender, number, date_of_birth,
             subject, hobbies, file, address, state, city):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.gender = gender
    self.number = number
    self.date_of_birth = date_of_birth
    self.subject = subject
    self.hobbies = hobbies
    self.file = file
    self.address = address
    self.state = state
    self.city = city