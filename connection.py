import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost', charset='utf8'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
        self.charset = charset

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset=self.charset
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Subscriber:
    def __init__(self, db_connection, name, email):
        self.db_connection = db_connection.connection
        self.name = name
        self.email = email

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO myapp_subscribers  VALUES (%s, %s);", (self.name, self.email))
        self.db_connection.commit()
        c.close()


con = Connection(user='dbuser', password='123', db='tutoring')

with con:
    obj = Subscriber(con, '1', '1')
    obj.save()
