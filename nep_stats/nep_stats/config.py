from contextlib import contextmanager
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker


DB_CONN = os.getenv(
    'DB_CONN', 'postgresql://postgres:password@localhost:5432/nep_stats')


engine = sqlalchemy.create_engine(DB_CONN)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
