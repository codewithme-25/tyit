PRACTICAL 10 - PROLOG

Q1. Batsman -> Cricketer -> Sportsman -> Famous Person

Write a Prolog program with the following:

Facts:
Define at least four batsmen (e.g. Sachin, Virat, Rohit, Dhoni).

Rules:
1. If X is a batsman, then X is a cricketer.
2. If X is a cricketer, then X is a sportsman.
3. If X is a sportsman, then X is a famous person.

Queries:
1. Check if Sachin is a cricketer.
2. Check if Virat is a sportsman.
3. List all famous persons.

Code:

batsman(sachin).
batsman(virat).
batsman(dhoni).
batsman(rohit).

cricketer(X) :- batsman(X).
sportsman(X) :- cricketer(X).
famous(X) :- sportsman(X).

Queries:

?- cricketer(sachin).
true.

?- sportsman(virat).
true.

?- famous(X).
X = sachin ;
X = virat ;
X = dhoni ;
X = rohit.


--------------------------------------------------


Q2. Teacher -> Employee -> Human -> Living Being

Write a Prolog program with the following:

Facts:
Define at least four teachers (e.g. Anita, Raj, Meena, Rahul).

Rules:
1. A teacher is an employee.
2. An employee is a human.
3. A human is a living being.

Queries:
1. Prove that Anita is a human.
2. Prove that Rahul is a living being.
3. List all humans.

Code:

teacher(anita).
teacher(raj).
teacher(meena).
teacher(rahul).

employee(X) :- teacher(X).
human(X) :- employee(X).
livingbeing(X) :- human(X).

Queries:

?- human(anita).
true.

?- livingbeing(rahul).
true.

?- human(X).
X = anita ;
X = raj ;
X = meena ;
X = rahul.


--------------------------------------------------


Q3. Student -> Learner -> Knowledge Seeker -> Future Professional

Write a Prolog program using the following relationship:

Student -> Learner -> Knowledge Seeker -> Future Professional

Define four students:
Riya, Amit, Sam and Neha.

Code:

student(riya).
student(amit).
student(sam).
student(neha).

learner(X) :- student(X).
knowledgeseeker(X) :- learner(X).
futureprofessional(X) :- knowledgeseeker(X).

Queries:

?- learner(riya).
true.

?- futureprofessional(amit).
true.

?- knowledgeseeker(X).
X = riya ;
X = amit ;
X = sam ;
X = neha.


--------------------------------------------------


Q4. Dog -> Animal -> Pet -> Living Being

Write a Prolog program using the following relationship:

Dog -> Animal -> Pet -> Living Being

Define four dogs:
Tommy, Bruno, Lucy and Rocky.

Code:

dog(tommy).
dog(bruno).
dog(lucy).
dog(rocky).

animal(X) :- dog(X).
pet(X) :- animal(X).
livingbeing(X) :- pet(X).

Queries:

?- pet(tommy).
true.

?- livingbeing(bruno).
true.

?- livingbeing(X).
X = tommy ;
X = bruno ;
X = lucy ;
X = rocky.


--------------------------------------------------


Q5. Book -> Knowledge Source -> Educational Material -> Valuable Resource

Write a Prolog program using the following relationship:

Book -> Knowledge Source -> Educational Material -> Valuable Resource

Define four books:
Physics, Math, History and Computer.

Code:

book(physics).
book(math).
book(history).
book(computer).

knowledgesource(X) :- book(X).
educationalmaterial(X) :- knowledgesource(X).
valuableresource(X) :- educationalmaterial(X).

Queries:

?- educationalmaterial(math).
true.

?- valuableresource(physics).
true.

?- valuableresource(X).
X = physics ;
X = math ;
X = history ;
X = computer.


--------------------------------------------------


Q6. Family Tree

Write a Prolog program to represent family relationships using male,
female and parent facts. Define rules for father, mother, grandfather,
grandmother, sibling and ancestor.

Code:

male(john).
male(mike).
male(david).

female(lisa).
female(susan).
female(anna).

parent(john, mike).
parent(john, lisa).
parent(susan, mike).
parent(susan, lisa).
parent(mike, david).
parent(anna, david).

father(F, C) :-
    male(F),
    parent(F, C).

mother(M, C) :-
    female(M),
    parent(M, C).

grandfather(GF, C) :-
    male(GF),
    parent(GF, P),
    parent(P, C).

grandmother(GM, C) :-
    female(GM),
    parent(GM, P),
    parent(P, C).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

ancestor(A, C) :-
    parent(A, C).

ancestor(A, C) :-
    parent(A, P),
    ancestor(P, C).
