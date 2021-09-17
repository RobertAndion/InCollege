from index import *


class TestIsPasswordSecure():
    def test_password_character_limit_lower(self):
        assert is_password_secure("P2$s") == False
        assert is_password_secure("") == False
        assert is_password_secure("P2$swor") == False

        assert is_password_secure("P2$sword") == True
        assert is_password_secure("P2$sword12") == True

    def test_password_character_limit_upper(self):
        assert is_password_secure("P2$swordTooLong123") == False
        assert is_password_secure("Pa$sword12345") == False
        assert is_password_secure("Pa$sword1234") == True
        assert is_password_secure("Pa$sword123") == True

    def test_password_contains_capital(self):
        assert is_password_secure("password1#") == False
        assert is_password_secure("Password1#") == True

        assert is_password_secure("1$c456789") == False
        assert is_password_secure("A$c456789") == True

    def test_password_contains_lowercase(self):
        assert is_password_secure("PASSWORD1#") == False
        assert is_password_secure("PASSWORd1#") == True

        assert is_password_secure("1$C456789") == False
        assert is_password_secure("a$C456789") == True

    def test_password_contains_number(self):
        assert is_password_secure("Password$$") == False
        assert is_password_secure("Password1$") == True

    def test_password_contains_special(self):
        assert is_password_secure("Password12") == False
        assert is_password_secure("Password1#") == True
