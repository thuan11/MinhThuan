#in day so va tinh tong cac so chan cua day 

n=input("nhap n: ")
tong=0
print"day so tu 1 den n !"
for x in range(1,n+1):
	print x 
	if((x%2) == 0):
		tong=tong+x
print"tong: ",tong 
	
