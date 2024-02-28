import os
import gzip
from domains.management_system import StudentManagementSystem

def compress_files():
    files_to_compress = ["main.py", "input.py", "output.py", "domains/", "students.txt", "courses.txt", "marks.txt"]
    with gzip.open("students.dat", "wb") as f_out:
        for file in files_to_compress:
            if os.path.isfile(file):
                with open(file, "rb") as f_in:
                    f_out.write(f_in.read())
            elif os.path.isdir(file):
                for root, dirs, files in os.walk(file):
                    for name in files:
                        path = os.path.join(root, name)
                        with open(path, "rb") as f_in:
                            f_out.write(f_in.read())

def decompress_files():
    if os.path.isfile("students.dat"):
        with gzip.open("students.dat", "rb") as f_in:
            with open("main.py", "wb") as f_out:
                f_out.write(f_in.read())
        print("Decompression successful.")
    else:
        print("No compressed file found.")

if __name__ == "__main__":
    decompress_files()

    sms = StudentManagementSystem()
    sms.main()

    with open("students.txt", "a") as f:
        f.write("=====\n")
    with open("courses.txt", "a") as f:
        f.write("=====\n")
    with open("marks.txt", "a") as f:
        f.write("=====\n")

    compress_files()