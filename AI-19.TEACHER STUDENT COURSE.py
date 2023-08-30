% Facts
teacher(john, math).
teacher(amy, science).
teacher(susan, history).

student(alex, math).
student(lisa, science).
student(mike, history).
student(sara, science).

subject(math, 101).
subject(science, 202).
subject(history, 303).

% Rules
teaches(Teacher, Subject) :- teacher(Teacher, Subject).

studies(Student, Subject) :- student(Student, Subject).

subject_code(Subject, Code) :- subject(Subject, Code).
