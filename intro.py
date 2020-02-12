# printing
print('Hello World!')

# assignment
my_animals = ("dog", "cat", "fish")
print(my_animals)

# function and loops


def print_lyrics(x):
    for i in range(x):
        print("Alright")


print_lyrics(10)

# conditionals


def what_do(x):
    if x:
        print('this was true')
    else:
        print('this was false')


what_do(True)
what_do(False)

# exercise 4


def right_justify(s):
    # add spaces until len(s) is greater than or equal to 70
    output = s
    while len(output) < 70:
        output = " " + output
    return output


print(right_justify("does this work?"))


def right_justify_better(s):
    # calculate how many spaces to add
    spaces = ((70 - len(s)) * " ")
    return spaces + s


print(right_justify_better("does this work2?"))

# Challenge
# Exercise 1


def get_seconds(mins, secs):
    return "There are " + str(mins * 60 + secs) + " seconds in " + str(mins) + " min and " + str(secs) + " seconds."


print(get_seconds(21, 15))

# Exercise 2


def get_miles(km):
    return "There are " + str(km / 1.60934) + " miles in " + str(km) + " kilometers."


print(get_miles(5))

# Exercise 3


def get_minutes_from_seconds(secs):
    minutes = int(secs / 60)
    print('total seconds', secs)
    print('these are minutes', minutes)
    return [minutes, secs % 60]


def get_pace_in_miles(km, mins, secs):
    miles = km / 1.60934
    total_seconds = mins * 60 + secs
    secs_per_mile = total_seconds / miles
    time = get_minutes_from_seconds(secs_per_mile)
    return "You ran " + str(miles) + " miles at " + str(time[0]) + " minutes " + str(time[1]) + " seconds per mile."


print(get_pace_in_miles(5, 21, 15))


def do_four(f):
    do_twice(f)
    do_twice(f)


def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)
print("starting do_four")
do_four(print_spam)


# Exercise 4 - Fermat's Last Theorem


def check_fermant(a, b, c, n):
    if c**n == a**n + b**n:
        return "Fermant was wrong."
    else:
        return "No, that doesn't work."


print(check_fermant(2, 4, 5, 3))


def prompt_fermat():
    print("Input a")
    a = int(input())
    print("Input b")
    b = int(input())
    print("Input c")
    c = int(input())
    print("Input n")
    n = int(input())
    return check_fermant(a, b, c, n)


# print(prompt_fermat())

arr = [1, 2, 3, 4, 1, 2]
print(arr)
arr.remove(1)
print(arr)

car = {"brand": "Honda", "model": "CR-V", "year": 2002}
print(car.get("brand"))
print(car["brand"])
