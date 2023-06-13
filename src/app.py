from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

# 宣告對映
Base = declarative_base()

class User(Base):  # 此為 2. python class  -> 通常會放在 models.py 裡面
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)

# 連結SQLite3資料庫example.db
engine = create_engine('sqlite:///example.db')

# 建立Schema
Base.metadata.create_all(engine)  # 相當於Create Table