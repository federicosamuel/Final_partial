https://replit.com/join/rzvawhgvkg-federicoolmos1

version= 0
no=0

readings = int(input("What is the number of readings:"))

while version < int(readings):
  version+= 1
  temp= float(input("Insert temperature of each:"))
  if temp < 10 or temp > 40:
    no+= 1 

error = (no*100)/readings

print("The sensor went wrong", no, "times")
print("The sensor went wrong", error, "% of the time")
