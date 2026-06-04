import os
import time

from watchdog.observers import Observer

from handlers.file_handlers import FileHandler
from core.logger import write_log


def start_monitor(
    path,
    original_hash,
    backup_path
):

    """
    Start monitoring a protected file.
    """

    path = os.path.abspath(path)

    event_handler = FileHandler(
        path,
        original_hash,
        backup_path
    )

    observer = Observer()

    watch_dir = os.path.dirname(path)

    observer.schedule(
        event_handler,
        path=watch_dir,
        recursive=False
    )

    observer.start()

    print("Monitoring started...")

    write_log(
        f"Monitoring started for {os.path.basename(path)}"
    )

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

        write_log(
            "Monitoring stopped"
        )

    observer.join()