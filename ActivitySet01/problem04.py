# Conditional Execution

hours=int(input("Enter number of hours"))
rate=float(input("Enter rate"))
if (hours<=40):
  pay=hours*rate
elif (hours>40):
  pay=(rate*40)+((hours-40)*(rate*1.5))
print(pay)
