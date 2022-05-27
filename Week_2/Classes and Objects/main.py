class Student:
    # [assignment] Skeleton class. Add your code here   

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def __repr__(self):
        return "name:%s,\n age: %s, \n tracks:%s, \n score:%s" % (self.name, self.age, self.tracks, self.score)

    def __str__(self):
        return "name:%s,\n age: %s, \n tracks:%s, \n score:%s" % (self.name, self.age, self.tracks, self.score)

    
    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob)
