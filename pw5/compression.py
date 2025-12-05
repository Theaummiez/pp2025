import os
import zipfile

ARCHIVE_NAME = "students.dat"

FILES_TO_COMPRESS = [
    "students.txt",
    "courses.txt",
    "marks.txt"
]

def compress_data():
    """Compress selected files into students.dat"""
    with zipfile.ZipFile(ARCHIVE_NAME, "w", zipfile.ZIP_DEFLATED) as archive:
        for filename in FILES_TO_COMPRESS:
            if os.path.exists(filename):
                archive.write(filename)
                print(f"Compressed: {filename}")
            else:
                print(f"Skipped (not found): {filename}")


def decompress_data():
    """Extract students.dat if it exists"""
    if not os.path.exists(ARCHIVE_NAME):
        return False

    with zipfile.ZipFile(ARCHIVE_NAME, "r") as archive:
        archive.extractall()
        print("Archive extracted.")

    return True
