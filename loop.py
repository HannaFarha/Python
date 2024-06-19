n=1
while True:
    print(n)
    n +=1
    if n>10:
        break

print("finish")

x="rewwddfdfdsfsiokdjjdjhldkjx"

d=dict()
for c in x:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print(d)