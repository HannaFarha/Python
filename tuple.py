t=("a","b")
print (type(t))
s="my name is Hanna Farha i am from Syria but living in Germany"

words = s.split()
l = list()
for word in words :
    l.append((len(word),word))
l.sort(reverse=True)
print(l)