import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)

if(hour>=4 and hour<12):
    print("good morning sir/ma'am")
elif(hour>=12 and hour<17):
    print("good afternoon sir/ma'am") 
elif(hour>=17 and hour<20):
    print("good evening sir/ma'am")  
elif(hour>=20 and hour<4):
    print("good evening sir/ma'am")         