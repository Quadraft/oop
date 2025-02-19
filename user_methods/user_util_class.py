import random
import re
import datetime

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = datetime.now().year % 100
        random_digits = random.randint(100000, 999999)
        return int(f"{year}{random_digits}")

    @staticmethod
    def generate_password():
        import string
        import random
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        return password

    @staticmethod
    def is_strong_password(password):
        if (len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            return True
        return False

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None