#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import json
import logging

from flask import Flask
from flask_restful import Resource, Api

from defacto.utils.wrappers import log_route_call


LOGGER = logging.getLogger(__name__)
FLASK_APP = Flask(__name__)
REST_API = Api(FLASK_APP)


class HelloWorld(Resource):
    method_decorators = [log_route_call]

    def get(self):
        return "Not implemented", 404

    def post(self):
        return "Not implemented", 404


# Defines path with Resource class
REST_API.add_resource(HelloWorld, '/')
