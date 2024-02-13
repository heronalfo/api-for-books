from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String,Text, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///locals.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Books(Base):
    __tablename__ = 'Books'
    
    id = Column(Integer, primary_key=True)
    book = Column(String(100), nullable=False)
    author = Column(String(200), nullable=False)
    synopsis = Column(Text)
    created_at = Column(Date, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'book': self.book,
            'author': self.author,
            'synopsis': self.synopsis,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'content': self.content
        }

Base.metadata.create_all(engine)