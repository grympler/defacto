#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
from defacto.init_logging import init_logging
# FIXME: Set log level and formatter type.
init_logging(formatter_type="json")
from flask_cors import CORS

# FIXME: Choose wich one.
import defacto.app as flask_app
# import defacto.app_rest as flask_app


app = flask_app.FLASK_APP
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
