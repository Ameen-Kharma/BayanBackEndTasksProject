import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

driver = 'mysql+mysqldb'
database_name = 'bayan'
name = 'root'
dabase_password = 'root'
host = 'localhost'
port = 3306


SQLA_ENGINE = '{driver}://{name}:{password}@{host}:{port}/{database_name}'.format(driver=driver, name=name,
                                                                                  password=dabase_password, host=host,
                                                                                  port=port,
                                                                                  database_name=database_name)

engine = sqlalchemy.create_engine(SQLA_ENGINE, echo=True)

Session = sessionmaker(bind=engine)

# session_factory = sessionmaker(bind=engine)
# Session = scoped_session(session_factory)
db_session = Session()
