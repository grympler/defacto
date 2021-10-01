#!/usr/bin/env python
"""Module gathering helper wrappers."""
from datetime import datetime
from functools import wraps
import logging
import traceback

from flask import jsonify, request


LOGGER = logging.getLogger(__name__)


def log_route_call(fun):
    """Log a route call.

    extra logging dict args must contains following fields:
        * query
        * backtrace (if present)
        * error message (if present)
        * api response
    """
    @wraps(fun)
    def wrapper(*args, **kwargs):
        """Wrapper for flask route logging."""

        extra = {
            "route": request.path
        }
        status_code = 200
        try:
            query = request.json
            time0 = datetime.now()
            response = fun(query, *args, **kwargs)
            elapsed_time = datetime.now() - time0
            extra.update({"elapsed_time": elapsed_time.total_seconds()})
        # TODO: Add custom Exception handling.
        except Exception as err:
            response = {"message": "Internal Error"}
            extra.update({
                "traceback": traceback.format_exc(),
                "error": f"{err}"
            })
            status_code = 500

        extra.update({
            "response": response,
            "status_code": status_code,
            "query": query or request.data
        })

        if status_code == 200:
            LOGGER.info("Response", extra=extra)
        else:
            LOGGER.error("Response", extra=extra)

        api_response = jsonify(response)
        api_response.status_code = status_code
        return api_response

    return wrapper
