import os
import signal


def before_scenario(context, _):
    # Set up context object for later use
    context.hash_objects = []
    context.stats = {"total_requests": None,
                     "average_time": None,
                     "status_code": None}


def after_tag(context, tag):
    if tag != "shutdown":
        os.kill(context.app_pid, signal.SIGTERM)
