from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import Column,Integer,String,DateTime,func,ForeignKey
import asyncio
from datetime import datetime

engine=create_async_engine(url="postgresql+asyncpg://postgres:main@localhost/qrlink")

SessionLocal=async_sessionmaker(engine,expire_on_commit=False,autoflush=False)


def get_db():
    with SessionLocal as db:
            yield db
    

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'

    user_id:Mapped[str]=mapped_column(nullable=False,unique=True,primary_key=True)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,default=func.now())
    user_history=relationship("user_history",back_populates="User")

class QRCode(Base):
    __tablename__="qr_codes"

    user_id:Mapped[str]=mapped_column(String,ForeignKey("users.user_id"))
    qr_id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    encoded_qr:Mapped[str]=mapped_column(nullable=False,unique=True)
    user=relationship("User",back_populates="users")

class Link(Base):
    __tablename__="link"

    user_id:Mapped[str]=mapped_column(ForeignKey("users.user_id"))
    link_id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    links:Mapped[str]=mapped_column(nullable=False,unique=True)
    user=relationship("User",back_populates="users")