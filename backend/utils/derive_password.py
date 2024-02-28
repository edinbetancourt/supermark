# Config
from project import settings

class DerivePassword:

    # keylog_file = "./backend/media/txt/keylog.txt"
    keylog_file = settings.KEYLOG_FILE
    
    def get_password(self):
        """ Build the password """

        print(self.keylog_file)


        password = ''

        try:
            with open(self.keylog_file, "r") as file:
                for content in file:
                    key = content.strip()

                    # Build the password
                    if not key in password:
                        password = password + key

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
