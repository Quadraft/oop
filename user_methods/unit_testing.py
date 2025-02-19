import unittest
from datetime import datetime
from user_class import User
from user_service_class import UserService
from user_util_class import UserUtil

class TestUser(unittest.TestCase):
    def test_get_details(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "Password123!", datetime(1990, 1, 1))
        self.assertEqual(user.get_details(), "User ID: 1, Name: John Doe, Email: john.doe@example.com, Birthday: 1990-01-01")

    def test_get_age(self):
        user = User(1, "John", "Doe", "john.doe@example.com", "Password123!", datetime(1990, 1, 1))
        self.assertEqual(user.get_age(), datetime.today().year - 1990)

class TestUserService(unittest.TestCase):
    def setUp(self):
        UserService.users = {}  # Clear the users dictionary before each test
        self.user = User(1, "John", "Doe", "john.doe@example.com", "Password123!", datetime(1990, 1, 1))
        UserService.add_user(self.user)

    def test_add_user(self):
        self.assertEqual(UserService.get_number(), 1)

    def test_find_user(self):
        self.assertEqual(UserService.find_user(1), self.user)

    def test_delete_user(self):
        UserService.delete_user(1)
        self.assertIsNone(UserService.find_user(1))

    def test_update_user(self):
        updated_user = User(1, "Jane", "Doe", "jane.doe@example.com", "Password123!", datetime(1990, 1, 1))
        UserService.update_user(1, updated_user)
        self.assertEqual(UserService.find_user(1).name, "Jane")

class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(isinstance(user_id, int) and len(str(user_id)) == 8)

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertFalse(UserUtil.is_strong_password(password))

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("Password123!"))
        self.assertFalse(UserUtil.is_strong_password("weak"))

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@example.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("john.doe@com"))

if __name__ == '__main__':
    unittest.main()