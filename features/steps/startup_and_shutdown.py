from behave import *
from assertpy import assert_that
from subprocess import Popen
import platform
import time
from psutil import process_iter, ZombieProcess


def check_process():
    # process.name() throws ZombieProcess on macOS if recently terminated
    for process in process_iter():
        try:
            if "broken-hashserve" in process.name():
                return True
        except ZombieProcess:
            pass
    return False


@given("the user launches the application")
def step_impl(context):
    os_type = platform.system()

    if os_type == "Linux":
        executable = "lib/broken-hashserve_linux"
    elif os_type == "Darwin":
        executable = "lib/broken-hashserve_darwin"
    elif os_type == "Windows":
        executable = "lib/broken-hashserve_win.exe"
    else:
        raise NotImplementedError(f"{os_type} not supported")

    #  Save the process id so we can kill it later
    context.app_pid = Popen(executable).pid

    #  Wait to ensure the application has started
    time.sleep(0.5)


@then("the application is running")
def step_impl(context):
    assert_that(check_process()).described_as("application is running").is_true()


@then("the application is not running")
def step_impl(context):
    assert_that(check_process()).described_as("application is running").is_false()
