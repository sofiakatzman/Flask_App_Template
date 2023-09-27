from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Milestone, User, Aspect, Friend)

if __name__ == '__main__':
    engine = create_engine("sqlite:////instance/app.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()