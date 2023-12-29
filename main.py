import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

dir_path = "C:/Users/Owner/Downloads"

with os.scandir(dir_path) as entries:
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()