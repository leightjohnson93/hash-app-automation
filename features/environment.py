import os
import signal

# def before_all(context):
#     context.app_pid = 0

def after_scenario(context, scenario):
    print(context.app_pid)
    scenario.context.app_pid
    os.kill(context.app_pid, signal.SIGTERM)