Implement a group class - Group. The group instance must have attributes - name - (describes the individual name of the group), students - a container (list/set/dictionary - at your choice) - into which you can add/remove students (instances of the Student class).
Adding/removing must be implemented using the methods of the Group class - respectively - add_student(obj: Student)/remove_student(obj: Student).
Hint: to add/remove a Student, you may need to compare instances of the Student class with each other - for this you will need to implement specialized methods in the Student class.
Hint - if you choose a set to store Student instances in the Group class, the Student instances must become immutable (hashed). You can read about how to implement this here.
The Group class must provide the following functionality:
len(Group()) -> returns an integer, the number of students in the group
comparison of groups: ==, !=, >, <, >=, <= - is implemented based on comparing the number of students in the group
addition of groups - gr_1: Group + gr_2: Group -> returns an instance of the Group class, the name of which is formed as a concatenation of the names gr_1 and gr_2, and the composition of students is the sum of the compositions of students of both groups.
If a student is in gr_1 and gr_2, then he must appear in the group formed as a result of their addition only once.

UPD. create a method for the Group class that will receive the path to the file and the Student class, and return an instance of the Group class in the students attribute of which Student() instances are added, created according to the entries in the file.
