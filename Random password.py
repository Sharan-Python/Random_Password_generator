import random
import os

random.random()
list1 = [
    "A" "b" "c" "D"  "i" "j" "k" " " "m" "n" "O" "+" "q" "r" "s" "t" "u" "v " "W" "¬¬" "|" "z" "£" "%" "*" "(" ")" "¬" "`" "<" ">" "?" "_" "/" "~"]
q = random.choice(list1[0])
q2 = random.choice(list1[0])
q3 = random.choice(list1[0])
q4 = random.choice(list1[0])
q5 = random.choice(list1[0])
q6 = random.choice(list1[0])
q7 = os.urandom(3)  # This function of os module is used in real life cryptography
q8 = random.SystemRandom()
y = str(q8)
f = y.strip("<random.SystemRandom object at>")
# print(f)
f = str(f)
x = str(q7)
print(q4 + x + q + q3 + q5 + f + q + q + q2 + q3 + q5 + q6 + x)
