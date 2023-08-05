a=True
b=False

print(a and a )#True
print(a and b)#False
print(a or b)#True
print(a or b)#False

print((3<4)and (4<5))# t y t -->t
print((3<4)and (6<5))# T and F-->False

#negación
resultado= a and a # T and T
print(resultado)
print(not resultado)