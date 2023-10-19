C_m , G_m = map(int,input().split(" "))
C_s , G_s = map(int,input().split(" "))
rate = int(input())

C_m = C_m + G_m * rate
C_s = C_s + G_s * rate

if C_m >= C_s:
    print("Yes")
else:
    print("No")