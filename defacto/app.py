#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import logging

from flask import Flask

from defacto.utils.wrappers import log_route_call


LOGGER = logging.getLogger(__name__)
FLASK_APP = Flask(__name__)


@FLASK_APP.route('/', methods=['POST'])
@log_route_call
def view(query, *args, **kwargs):
    """Main route of defacto project."""
    return {
        "status": "Success."
    }
