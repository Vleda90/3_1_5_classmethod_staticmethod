class Student:
    def __init__(self, first_name, last_name, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.major = major

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.major}'

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.age, self.major))

    def __eq__(self, other):
        return (isinstance(other, Student)
                and self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.major == other.major
                and self.age == other.age
        )
    @staticmethod
    def learn():
        print("I'm learning")

    def do_nothing(self):
        pass


class Group:
    def __getitem__(self, key):
        students_list = list(self.students)
        if isinstance(key, int):
            return students_list[key]
        elif isinstance(key, str):
            for student in students_list:
                if student.first_name == key or student.last_name == key:
                    return student
            raise KeyError(f"Student with name '{key}' not found")
        else:
            raise TypeError("Index must be an integer or a string")

    def __init__(self, name: str):
        self.name = name
        self.students = set()


    def __repr__(self):
        return f'{self.name} {self.students}'


    def __iter__(self):
        self.students_list = list(self.students)
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.students_list):
            raise StopIteration
        student = self.students_list[self._index]
        self._index += 1
        return student


    def __eq__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'==' not supported between instances of {type(self)} and {type(other)}")
        return len(self) == len(other)


    def __ne__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'!=' not supported between instances of {type(self)} and {type(other)}")
        return len(self) != len(other)


    def __gt__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'>' not supported between instances of {type(self)} and {type(other)}")
        return len(self) > len(other)


    def __lt__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'<' not supported between instances of {type(self)} and {type(other)}")
        return len(self) < len(other)


    def __le__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'<=' not supported between instances of {type(self)} and {type(other)}")
        return len(self) <= len(other)


    def __ge__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'>=' not supported between instances of {type(self)} and {type(other)}")
        return len(self) >= len(other)


    def __add__(self, other):
        if not isinstance(other, Group):
            raise TypeError(f"'+'not supported between instances of {type(self)} and {type(other)}")
        new_group = Group(self.name + other.name)
        new_group.students = self.students | other.students

        return new_group

    @classmethod
    def create_from_file(cls, file_name: str, group_name: str, ):
        new_group = cls(group_name)
        file = None
        try:
            file = open(file_name, 'r')
            contents = file.readlines()
            for line in contents:
                line = line.strip('\n').split('_')
                first_name, last_name, age, major = line
                student = Student(first_name, last_name, age, major)
                new_group.add_student(student)
        except FileNotFoundError:
            print('File not found')
        finally:
            if file:
                file.close()
        return new_group


    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError(f"Adding not supported between instances of not {type(self)}. It should be {type(student)}")
        else:
            self.students.add(student)


    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)
            print(f"{self.name} removed from group")
        else:
            print(f"{self.name} not in group")


    def __len__(self):
        return len(self.students)

if __name__ == '__main__':
    gr1 = Group.create_from_file('students.txt', 'Group1')
    for i in range(10):
        print(gr1[i])

