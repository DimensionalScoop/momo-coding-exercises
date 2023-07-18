with open("momo_d3/input") as file:
    lines = [line.rstrip() for line in file]

tasche1 = []
tasche2=[]
for l in lines:
    size = len(l)
    half = int(size/2)
    tasche1.append(l[0:half])
    tasche2.append(l[half:size])

    assert size == (len(tasche1[-1]) + len(tasche2[-1]))

double = []
for t1, t2 in zip(tasche1, tasche2):
    share = []
    for letter in t1:
        if t2.count(letter) > 0:
            if share.count(letter) == 0:
                share.append(letter)
    for s in share:
        double.append(s)

print(double)

value = 0
for l in double:
    if l.isupper():
        value += ord(l) - 38
    else:
        value += ord(l) -96

print(value)