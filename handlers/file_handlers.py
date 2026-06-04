import os

from watchdog.events import FileSystemEventHandler

from core.integrity import generate_hash
from core.recovery import restore_file
from core.protection import make_read_only
from core.logger import write_log
from core.alerts import show_alert


class FileHandler(FileSystemEventHandler):

    def __init__(
        self,
        file_path,
        original_hash,
        backup_path
    ):

        self.file_path = os.path.abspath(
            file_path
        )

        self.original_hash = original_hash

        self.backup_path = backup_path

        self.restoring = False

    def on_modified(
        self,
        event
    ):

        # Ignore directories
        if event.is_directory:
            return

        # Prevent recursive restore events
        if self.restoring:
            return

        changed_path = os.path.abspath(
            event.src_path
        )

        # Ignore other files
        if changed_path != self.file_path:
            return

        try:

            current_hash = generate_hash(
                self.file_path
            )

            if current_hash != self.original_hash:

                show_alert(
                    "Unauthorized modification detected!"
                )

                write_log(
                    f"Tampering detected: {os.path.basename(self.file_path)}"
                )

                self.restoring = True

                restore_file(
                    self.backup_path,
                    self.file_path
                )

                make_read_only(
                    self.file_path
                )

                write_log(
                    "File restored successfully"
                )

                print(
                    "Original file restored."
                )

                self.restoring = False

        except Exception as e:

            write_log(
                f"Error during monitoring: {e}"
            )

            print(
                f"Monitoring Error: {e}"
            )