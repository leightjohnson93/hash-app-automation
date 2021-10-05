import os
import signal


def before_scenario(context, _):
    # Set up context object for later use
    context.hash_objects = []
    context.stats = {"total_requests": None, "average_time": None, "status_code": None}


def after_scenario(context, _):
    # Swallow exception in case app isn't running
    try:
        os.kill(context.app_pid, signal.SIGTERM)
    except OSError:
        pass
