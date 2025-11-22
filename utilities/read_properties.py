import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info", "baseUrl")
        return url

    @staticmethod
    def getUserEmail():
        user_email = config.get("common info", "user_email")
        return user_email

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
