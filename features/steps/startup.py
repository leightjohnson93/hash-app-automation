from behave import *
import platform
import subprocess

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
        
    context.app_pid = subprocess.Popen(executable).pid
