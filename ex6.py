types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
#the joke is in binary 10 means two so it reads there are two types of people but you need to know binary in order to get the joke 

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)
