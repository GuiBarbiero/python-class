# 1
a = [1,2,3,4,5,6]
b = [3,4,5,6,7,7]

aa = set(a)
bb = set(b)
print(aa)
print(bb)

c = aa & bb
print(c)

#2
d = aa - bb
print(d)

#3
e = bb - aa
print(list(e))

# 4
f = d ^ e
print(f)

