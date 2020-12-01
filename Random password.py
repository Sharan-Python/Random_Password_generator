import random
import os

random.random()
list1 = [
    "a" "b" "c" "d"  "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "£" "%" "*" "(" ")" "¬" "`" "<" ">" "?" "_" "/" "~"]
q = random.choice(list1[0])
q2 = random.choice(list1[0])
q3 = random.choice(list1[0])
q4 = random.choice(list1[0])
q5 = random.choice(list1[0])
q6 = random.choice(list1[0])
q7 = os.urandom(4)  # This function of os module is used in real life cryptography
x = str(q7)
print(q2 + q4 + x + q6 + q + q3 + q5)
