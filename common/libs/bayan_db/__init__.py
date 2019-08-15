import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

driver = 'mysql+mysqldb'
database_name = 'bayandatabase'
name = 'root'
dabase_password = ''
host = 'localhost'
port = 3308


SQLA_ENGINE = '{driver}://{name}:{password}@{host}:{port}/{database_name}'.format(driver=driver, name=name,
                                                                                  password=dabase_password, host=host,
                                                                                  port=port,
                                                                                  database_name=database_name)

engine = sqlalchemy.create_engine(SQLA_ENGINE)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
db_session = Session()