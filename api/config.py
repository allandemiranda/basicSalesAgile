DEBUG = True

pg_user = "allanmiranda"
pg_pwd = "senha123"
pg_port = "5432"
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost:{port}/agile_db".format(
    username=pg_user, password=pg_pwd, port=pg_port)
SQLALCHEMY_TRACK_MODIFICATIONS = True

BCRYPT_LOG_ROUNDS = 10