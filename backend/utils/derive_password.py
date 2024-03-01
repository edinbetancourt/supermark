# Config
from project import settings

class DerivePassword:

    # keylog_file = "./backend/media/txt/keylog.txt"
    keylog_file = settings.KEYLOG_FILE
    
    def get_password(self):
        """ Build the password """

        password = ''

        try:

            with open(self.keylog_file, "r") as file:
                
                # New code
                number = []
                for key in file:
                    key = key.strip()
                    # number.insert(0, key)
                    number.append(key)

                for key in number:
                    digit = key

                    for value in digit:

                        # Build the password
                        if not value in password:
                            password = password + value

                return password

        except FileNotFoundError:
            return None

    def get_key_list(self):
        """ Get key list from file """

        key_list = []

        try:
            with open(self.keylog_file, "r") as file:
                for content in file:
                    key_list.append(content.strip())

                return key_list

        except FileNotFoundError:
            return None
