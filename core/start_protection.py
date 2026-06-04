import threading
import json
import os

from core.recovery import create_backup
from core.integrity import generate_hash
from core.protection import make_read_only
from core.monitor import start_monitor
from core.logger import write_log


def protect_file(path):

    """
    Complete file protection workflow.
    """

    try:

        # Create backup
        backup_path = create_backup(path)

        # Generate original hash
        original_hash = generate_hash(path)

        # Make file read-only
        make_read_only(path)

        # Create metadata folder
        os.makedirs(
            "data/metadata",
            exist_ok=True
        )

        # Save status for frontend
        status = {

            "file": os.path.basename(path),

            "full_path": os.path.abspath(path),

            "status": "Protected",

            "monitoring": True
        }

        with open(
            "data/metadata/status.json",
            "w"
        ) as f:

            json.dump(
                status,
                f,
                indent=4
            )

        write_log(
            f"Protection enabled for {os.path.basename(path)}"
        )

        # Start monitoring in background
        monitor_thread = threading.Thread(
            target=start_monitor,
            args=(
                path,
                original_hash,
                backup_path
            )
        )

        monitor_thread.daemon = True

        monitor_thread.start()

        print(
            "File protected successfully."
        )

        return True

    except Exception as e:

        write_log(
            f"Protection failed: {e}"
        )

        print(
            f"Error: {e}"
        )

        return False