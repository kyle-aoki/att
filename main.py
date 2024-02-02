import subprocess
import sys
import threading
from time import sleep
from pynput.keyboard import Key, Listener

run_thread = None
started = False
stop_process = None


def pressed(key):
    global run_thread, started, stop_process
    if key == Key.f19:
        if started:
            stop_process()
        try:
            run_thread = threading.Thread(target=run)
            started = True
            run_thread.start()
        except Exception as e:
            print(e)


def run():
    global stop_process
    cmd = ' '.join(sys.argv[1:])
    subprocess.run("clear")
    print('starting process:', cmd)
    process = subprocess.Popen(cmd, shell=True)

    def stop():
        process.terminate()

    stop_process = stop
    process.wait()


keyboard_listener = Listener(on_press=pressed)

keyboard_listener.start()
keyboard_listener.join()
