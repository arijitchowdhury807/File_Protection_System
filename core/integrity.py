import hashlib


def generate_hash(path):

    """
    Generate SHA-256 hash of a file.
    """

    sha_hash = hashlib.sha256()

    with open(path, "rb") as f:

        while True:

            chunk = f.read(4096)

            if not chunk:
                break

            sha_hash.update(chunk)

    return sha_hash.hexdigest()