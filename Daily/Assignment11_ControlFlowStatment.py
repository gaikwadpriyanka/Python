# Control Flow Statement:-
#1.Selective statement -         if,if-elif-else,if-else
#2.Looping statement/iterrative - 
#3.Transfer statement/control

# nms =[1,2,3,4,88]
# for n in nms:
#     print(n)

nms2 = ['Anita','priyanka','Gorakh']
for n in nms2:
    if n.endswith('a'):
        print(n.upper())


# Assignment: 1.Print names in which i is present
#              2. Fetch names whose length is<=5
# 3. nums [23,10,70,45,100,35,7,8,16] fetch numbers divisible by 5 and 7
# Assignment:
# k =[1,1,1,2,2,3,4,5]- Fetch most frequent number from list means more than one

# k =[1,1,1,2,2,3,4,5]
# s=set()
# for i in k:
#     if(k.count(i)>1):
#         s.add(i)
# print(s)
          
# s1={}
# print(type(s1))

# While to check correct pin of ATM card
count=3
pin = input('Enter  the pin')
while(pin!='1234'and count>0):
    print(count,end='')
    pin = input('Attempt left, please Enter correct  pin')
    count-=1

if(count<=0):
    print('you tried multiple time, login failed')
else:
    print("Login Successfull")