arr=[7,9,9,5,7,8,5,0]
print(set(arr))                  #set removes all the duplicates
m,n=tuple(map(int,input().split()))  # great merhod
print(m,n)
d=input().split()   #if not set it is list by default
print("first element: ",d[0])


for i in range(101,-1,-2):  #loop 3 arguments
 print(i,end=" ")


#seperarion
word="kasdhfkjaskudf"
b=3
h=[word[i:i+b] for i in range(0, len(word), b)]
print(h)
