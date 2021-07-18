inp = input("Europe floor: ")
usf = int(inp) + 1
print("US Floor", usf)

count = 0 
sum = 0
print("before", count , sum)
for value in [ 3,2,4,5,2]:
   count = count + 1
   sum = sum + value
   print(count, sum, value)
print("After",count, sum, sum/count)

found = False
print("before", found)
for value in [ 3,2,4,5,2,1,2]:
   if value == 2:      
      found = True
      print(found, value)
      break
print("After", found)

smallest = None
print("before")
for value in [ 3,5,10,25,42,61,32]:
   if smallest is None:
      smallest = value
   elif value < smallest:
      smallest = value
   print(smallest, value)
print("After", smallest)


   