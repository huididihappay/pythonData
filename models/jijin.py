# !/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import Column, String, Integer, DateTime,Float,BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Jjjin(Base):
    __tablename__ = 'jijin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(16))
    name = Column(String(64))
    manager = Column(String(64))
    company = Column(String(64))
    scale = Column(Float(10,2))
    create_time = Column(DateTime)
    jijin_time = Column(DateTime)

    def __init__(self, code, name):
        self.code = code
        self.name = name

class Gupiao(Base):
    __tablename__ = 'gupiao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(16))
    gu_code = Column(String(6))
    gu_name = Column(String(64))
    scale = Column(String(16))


    def __init__(self, code, gu_name,gu_code,scale):
        self.code = code
        self.gu_name = gu_name
        self.gu_code = gu_code
        self.scale = scale

class Beixiang(Base):
    __tablename__ = 'beixiang'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(6))
    name = Column(String(64))
    num = Column(BigInteger)
    scale = Column(Float(10.2))
    today_time = Column(DateTime)


    def __init__(self, code, name,num,scale,today_time):
        self.code = code
        self.name = name
        self.num = num
        self.scale = scale
        self.today_time = today_time

class  RuanjianCeshi(Base):
    __tablename__ = 'ruanjianceshi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    salary = Column(String(10))
    year = Column(String(64))
    xueli = Column(BigInteger)
    miaoshu = Column(String(900000))
    name = Column(String(64))

    def __init__(self, salary, year, xueli, miaoshu, name):
        self.salary = salary
        self.year = year
        self.xueli = xueli
        self.miaoshu = miaoshu
        self.name = name



