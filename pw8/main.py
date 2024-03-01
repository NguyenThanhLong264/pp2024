import os
import gzip
import pickle
import threading
from domains.management_system import StudentManagementSystem

def compress_files():
    files_to_compress = ["main.py", "input.py", "output.py", "domains/", "students.pickle", "courses.pickle", "marks.pickle"]
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

def pickle_persistence(sms):
    with open("students.pickle", "wb") as f:
        pickle.dump(sms.students, f)
    with open("courses.pickle", "wb") as f:
        pickle.dump(sms.courses, f)
    with open("marks.pickle", "wb") as f:
        pickle.dump(sms.marks, f)

def background_persistence(sms):
    threading.Timer(10.0, background_persistence, args=[sms]).start()  # Save every 10 seconds
    pickle_persistence(sms)

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Load data from pickles if they exist
    if os.path.isfile("students.pickle"):
        with open("students.pickle", "rb") as f:
            sms.students = pickle.load(f)
    if os.path.isfile("courses.pickle"):
        with open("courses.pickle", "rb") as f:
            sms.courses = pickle.load(f)
    if os.path.isfile("marks.pickle"):
        with open("marks.pickle", "rb") as f:
            sms.marks = pickle.load(f)

    # Start background thread for persistence
    background_persistence(sms)

    sms.main()

    with open("students.pickle", "wb") as f:
        pickle.dump(sms.students, f)
    with open("courses.pickle", "wb") as f:
        pickle.dump(sms.courses, f)
    with open("marks.pickle", "wb") as f:
        pickle.dump(sms.marks, f)

    compress_files()