import hashlib
from random import random, randint
from brta import BRTA
from vehicles import Car, Bike, Cng
from ride_manager import uber

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()

        with open('users.txt', 'a') as file:
            duplicate_user = ''

            with open('users.txt', 'r') as read_file:
                users = read_file.readlines()
                for user in users:
                    if email in user:
                        duplicate_user = user.split(' ')[0]
            read_file.close()
            if duplicate_user == email:
                pass
                # print('This user already created')
            else:
                file.write(f'{email} {pwd_encrypted}\n')
                print(self.name, 'user Created')
        file.close()
        

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()

        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if stored_password == hashed_password:
            print('Valid user')
            return True
        else:
            print('Invalid User')
            return False


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license):
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        super().__init__(name, email, password)

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)

        if result == False:
            print('Sorry you are failed, try again')
        else:
            self.license = result
            self.valid_driver = True


    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'cng':
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)

        else:
            print('You are not a valid driver')


    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination



rider1 = Rider('Rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 50000)
rider2 = Rider('Rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 50001)
rider3 = Rider('Rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 50002)
rider4 = Rider('Rider4', 'rider4@gmail.com', 'rider4', randint(0, 30), 50003)
rider5 = Rider('Rider5', 'rider5@gmail.com', 'rider5', randint(0, 30), 50004)


driver1 = Driver('Driver1', 'driver1@gmail.com', 'driver1', randint(0, 30), 56286)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 12345, 10)

driver2 = Driver('Driver2', 'driver2@gmail.com', 'driver2', randint(0, 30), 56287)
driver2.take_driving_test()
driver2.register_a_vehicle('bike', 12345, 10)

driver3 = Driver('Driver3', 'driver3@gmail.com', 'driver3', randint(0, 30), 56288)
driver3.take_driving_test()
driver3.register_a_vehicle('cng', 12345, 10)

driver4 = Driver('Driver4', 'driver4@gmail.com', 'driver4', randint(0, 30), 56289)
driver4.take_driving_test()
driver4.register_a_vehicle('car', 12345, 10)

driver5 = Driver('Driver5', 'driver5@gmail.com', 'driver5', randint(0, 30), 56280)
driver5.take_driving_test()
driver5.register_a_vehicle('bike', 12345, 10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider1, 'car', 90)
