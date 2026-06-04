import os

from core.logger import write_log


def make_read_only(path):

    """
    Make file read-only.
    """

    try:

        os.chmod(path, 0o444)

        print(
            f"{path} is now read-only."
        )

        write_log(
            f"File made read-only: {os.path.basename(path)}"
        )

    except Exception as e:

        write_log(
            f"Failed to make file read-only: {e}"
        )

        print(
            f"Error: {e}"
        )


def make_writable(path):

    """
    Restore write permission.
    """

    try:

        os.chmod(path, 0o666)

        write_log(
            f"File made writable: {os.path.basename(path)}"
        )

    except Exception as e:

        write_log(
            f"Failed to make writable: {e}"
        )