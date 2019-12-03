#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/11 14:21
# @Author : Srunkyo
# @File   : example.py

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from models import SHOE_DATA, SHOE_IDS, SHOE_TITLES
parser = reqparse.RequestParser()
parser.add_argument('task')

app = Flask(__name__)
api = Api(app)


def abort_if_shoe_id_doesnt_exist(shoe_id):
    if shoe_id not in SHOE_IDS:
        abort(404, message="Shoe {} doesn't exist".format(shoe_id))

class ShoeByID(Resource):
    def get(self, shoe_id):
        abort_if_shoe_id_doesnt_exist(shoe_id)
        for d in SHOE_DATA:
            if (d['id'] == shoe_id):
                return d

class ShoeByTitle(Resource):
    def get(self, shoe_title):
        res = []
        for d in SHOE_DATA:
            if (shoe_title in d['title']):
                res.append(d)
        sorted_res = sorted(res, key=lambda i: i['price'])
        return sorted_res[:3]

class ShoeList(Resource):
    def get(self):
        return SHOE_DATA

api.add_resource(ShoeList, '/all')
api.add_resource(ShoeByID, '/id/<shoe_id>')
api.add_resource(ShoeByTitle, '/title_like/<shoe_title>')

if __name__ == '__main__':
    app.run(debug=True)
