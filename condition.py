start=int(input("Enter start number:"))
stop=int(input("Enter stop number:"))
for i in range(start, stop+1):
   if i%2 ==0:
      print(i,"even number")
   else:
      print("\t\t\t", i, "\todd number")