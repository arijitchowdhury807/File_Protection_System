import os

from core.logger import write_log


def show_alert(message):

    """
    Display and store security alerts.
    """

    # Create metadata directory
    os.makedirs(
        "data/metadata",
        exist_ok=True
    )

    # Terminal alert
    print(f"[ALERT] {message}")

    # Save alert for dashboard
    with open(
        "data/metadata/alert.txt",
        "w"
    ) as f:

        f.write(message)

    # Log alert
    write_log(
        f"ALERT: {message}"
    )