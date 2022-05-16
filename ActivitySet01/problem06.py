# Loops & Iterators
num = int(input("Enter a number?"))
largest = num
smallest = num

while True:
  num = input("Enter a number?")
  if num == "done":
      break
  try:
    num= int(num)
  except:
    print("Invalid input")
    continue
  if num>=largest:
      largest=num
  elif num<=smallest:
    smallest=num
  
print("Maximum is", largest)
print("Minimum is", smallest)
