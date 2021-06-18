#Exercise 1 count vowels in s

s = "azcbobobegghakl"
vowels = ["a","e","i","o","u"]
counter = 0
for i in s:
    for j in vowels:
        if j == i:
            counter += 1

print ("Number of vowels:", counter)

#Exercise 2 count "bob" in s

s="azcbobobegghakl"
found = "bob"
found_g = 0
x = 0
a = []
h=0
while x < len(s)-1:
    for j in s:
        a.append(j)
        x += 1

for l in a:
    if h <= len(s)-3:
        if a[h]+a[h+1]+a[h+2] == found:
            found_g +=1
        h += 1

print("Number of times", found, "occurs is:", found_g)

# Longest substring of s in which the letters occur in alphabetical order

s = "abcdaijopq"
r = ""
c = ""
for char in s:
    if (c == ""):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
if (len(c) > len(r)):
    r = c
print(r)


