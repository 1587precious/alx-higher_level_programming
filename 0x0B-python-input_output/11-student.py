class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

# Test the implementation
if __name__ == "__main__":
    import os
    import sys

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()

    print("Initial student:")
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    # Save to file
    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    # Reload from JSON
    new_student_1.reload_from_json(new_j_student_1)
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

