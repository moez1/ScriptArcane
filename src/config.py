import os


##########################################################################
# DataBase settings
##########################################################################
DB_USER = os.getenv("DB_USER", "arcane_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "arcane_pass")
DB_NAME = os.getenv("DB_NAME", "arcane")
DB_ADRESS = os.getenv("DB_ADRESS", "localhost:5432")
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADRESS}/{DB_NAME}"

##########################################################################
# twitter api settings
##########################################################################
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJVxWwEAAAAATjj2yuueRfH2JHFL1votRGnh48o%3DPbXbKu0rvQwOsaYx6l4J4P9hQ9pw8WvVMMRECQZkzM3psXK1lv"
APIKEYSECRET = "B40kRgixCUKDOGKqxAYpg8rJZcW5IRZRdFUB6TbzUzBKkjD55Y"
APIKEY = "LpTu8eQnEP0WVKbcj2fNa0cbo"


log_config = {
    "version":1,
    "root":{
        "handlers" : ["console"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    },
}