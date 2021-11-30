#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#expected output = 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#expected output = None 5 ->actual ouameError undefined)
tput = N
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#expected output = 10 ->actual output = 5 because return statement ends the function

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#expected output = 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#expected output = 5 None


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#expected output = 3 5 None ->actual output 3 5 and type error

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#expected output = 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#expected output = 100 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#expected output = 7 14 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#expected output = 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#expected output = 500 500 300 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#expected output = 500 500 300 300 ->acttual 500 500 300 500 returned the value but didnt redefine the variable


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#expected output = 500 500 300 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#expected output = 1 3 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#expected output = 1 3 5 10