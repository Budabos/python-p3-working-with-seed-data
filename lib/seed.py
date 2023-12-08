#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game,Base
fake=Faker()

fake = Faker()

if __name__ == '__main__':
    try:
        
        engine = create_engine('sqlite:///seed_db.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(Game).delete()
        games=[
            Game(
                title=fake.name(),
                genre=fake.word(),
                platform=fake.word(),
                price=fake.random.randint(0,50)

            )
            for i in range(50)]
       
        session.bulk_save_objects(games)
     
        session.commit()
    except Exception as e:
        print("encounted this error", str(e))    

     
     
    

   