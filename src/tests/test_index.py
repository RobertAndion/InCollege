import mock
import pytest
import src.index
from src.database_access import database_access as Database

class TestIsPasswordSecure:
    def test_password_character_limit_lower(self):
        assert src.index.is_password_secure("P2$s") == False
        assert src.index.is_password_secure("") == False
        assert src.index.is_password_secure("P2$swor") == False  # 7 chars
        assert src.index.is_password_secure("P2$sword") == True  # 8 chars
        assert src.index.is_password_secure("P2$sword12") == True

    def test_password_character_limit_upper(self):
        assert src.index.is_password_secure("P2$swordTooLong123") == False
        assert src.index.is_password_secure("Pa$sword12345") == False  # 13 chars
        assert src.index.is_password_secure("Pa$sword1234") == True  # 12 chars
        assert src.index.is_password_secure("Pa$sword123") == True

    def test_password_contains_capital(self):
        assert src.index.is_password_secure("password1#") == False
        assert src.index.is_password_secure("Password1#") == True

        assert src.index.is_password_secure("1$c456789") == False
        assert src.index.is_password_secure("A$c456789") == True

    def test_password_contains_lowercase(self):
        assert src.index.is_password_secure("PASSWORD1#") == False
        assert src.index.is_password_secure("PASSWORd1#") == True

        assert src.index.is_password_secure("1$C456789") == False
        assert src.index.is_password_secure("a$C456789") == True

    def test_password_contains_number(self):
        assert src.index.is_password_secure("Password$$") == False
        assert src.index.is_password_secure("Password1$") == True

    def test_password_contains_special(self):
        assert src.index.is_password_secure("Password12") == False
        assert src.index.is_password_secure("Password1#") == True


class TestUserAccess:
    def test_user_creation(self):
        input_values = ['randion', 'Password1#']
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        src.index.input = mock_input
        src.index.print = lambda s: output.append(s)
        src.index.register()

        assert output == [
        'Enter username: ',
        'Enter password: ', 
        'An account for randion was registered successfully... Redirecting\n'
        ]

        src.index.input = input
        src.index.print = print


@pytest.fixture(scope='module')
def db():
    # Setup
    db_name = "testing.sqlite3"
    db = Database.db(db_name)

    yield db

    # Teardown
    db.delete_users_table()
    db.close()


# class TestDB:
#     def test_register_user(self):
