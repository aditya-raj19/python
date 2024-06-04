import time
t=time.strftime('%H:%M:%S')
k=int(time.strftime('%H'))
if(k>=6 and k<=12):
    print('Good Morning')
elif(k>12 and k<=18):
    print("Good Afternoon")
else:
    print("Good Night")

print(t)