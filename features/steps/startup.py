from behave import *
from subprocess import Popen
import platform
import time


@given('the user launches the application')
def step_impl(context):
    os_type = platform.system()

    if os_type == 'Linux':
        executable = 'lib/broken-hashserve_linux'
    elif os_type == 'Darwin':
        executable = 'lib/broken-hashserve_darwin'
    elif os_type == 'Windows':
        executable = 'lib/broken-hashserve_win.exe'
    else:
        raise NotImplementedError(f'{os_type} not supported')

    #  Save the process id so we can kill it later
    context.app_pid = Popen(executable).pid

    #  Wait to ensure the application has started
    time.sleep(0.5)
