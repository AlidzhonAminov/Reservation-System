import psycopg2


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> psycopg2.connect:
        self.connection = psycopg2.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


