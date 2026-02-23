from faker import Faker

fake = Faker()

def get_login():
    return fake.email()

def get_password():
    return fake.password(10, False)

def get_firstname():
    return fake.first_name()