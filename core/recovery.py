import os
import shutil

from core.logger import write_log


def create_backup(path):

    """
    Create backup copy of file.
    """

    os.makedirs(
        "data/backups",
        exist_ok=True
    )

    filename = os.path.basename(path)

    backup_path = os.path.join(
        "data/backups",
        filename
    )

    shutil.copy2(
        path,
        backup_path
    )

    write_log(
        f"Backup created for {filename}"
    )

    return backup_path


def restore_file(
    backup_path,
    original_path
):

    """
    Restore original file
    from backup.
    """

    shutil.copy2(
        backup_path,
        original_path
    )

    write_log(
        f"File restored: {os.path.basename(original_path)}"
    )