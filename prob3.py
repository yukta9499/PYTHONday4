n = 1234
r = 0
for i in range(4):
    d = n %10
    n= n//10
    r = r * 10 + d
    
print(r)
