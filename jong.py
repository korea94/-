a = [5,20,35,10,8]
if a[0]>a[1] and a[0]>a[2] and a[0]>a[3] and a[0]>a[4]:
    print(a[0])
elif a[1]>a[2] and a[1]>a[3] and a[1]>a[4]:
    print(a[1])
elif a[2]>a[3] and a[2]>a[4]:
    print(a[2])
elif a[3]>a[4]:
    print(a[3])
else:
    print(a[4])