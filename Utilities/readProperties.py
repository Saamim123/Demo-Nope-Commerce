
import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config.get('common info','Baseurl')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def password():
        password=config.get('common info','password')
        return password
