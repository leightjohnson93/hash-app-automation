import os
import signal

def after_scenario(context, scenario):
    os.kill(context.app_pid, signal.SIGTERM)