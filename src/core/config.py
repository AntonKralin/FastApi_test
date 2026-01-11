import os

from dotenv import load_dotenv


load_dotenv(dotenv_path='../.env')


class DatabaseConfig:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.db_name = os.getenv("DATABASE_NAME")
        self.db_user = os.getenv("DATABASE_USER")
        self.db_password = os.getenv("DATABASE_PASSWORD")
        self.db_port = os.getenv("DATABASE_PORT")
        self.db_pool_size = 20
        self.db_max_overflow = 40


database_config = DatabaseConfig()


class ServerConfig:
    def __init__(self):
        self.host = os.getenv('HOST', '0.0.0.0')
        self.port = os.getenv('PORT', 8000)
        self.reload = os.getenv('RELOAD', True)


server_config = ServerConfig()
