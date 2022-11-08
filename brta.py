import random

class BRTA:
    def __init__(self) -> None:
        self.__licenses = {}

    def take_driving_test(self, email):
        score = random.randint(0, 100)
        if score >= 33:
            print('congrats, you have passed', score)
            license_number = random.randint(50000, 99999)
            self.__licenses[email] = license_number
            return license_number
        else:
            print('Sorry, you are failed', score)
            return False

    def validate_license(self, email, license):
        for key, value in self.__licenses.items():
            if key == email and value == license:
                return True
        return False