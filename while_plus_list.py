a=[1,2,3,4,5,6,7,8,9]
print("list a is:",a)
b=len(a)
print ("Length of a is:",b)
sum=20
i=0
while i<=8:
	print("now i is:",i)
	print("The",i,"value of a is",a[i])
	print("Present value of sum is:",sum)
	sum=sum+a[i]
	i=i+1
	print("New value of i is;",i) 
	print ("sum value of",i,"is:",sum)
