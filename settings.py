#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/13 14:45
# @Author : Srunkyo
# @File   : settings.py.py

CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    drivername="mysql+mysqldb",
    user="root",
    passwd="root",
    host="localhost",
    port="3306",
    db_name="savary",
)