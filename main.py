
#House Rules: How many dishes are in the sink? If there are less than 5 dishes in the sink, then you can forget about the dishes and eat a snack. If the number of disehs equals 10, then you must wash them immediately. If there are more than 20 dishes, than you must run the dishwasher.

dishes = input("How many dishes are in the sink? ")
dishes=int(dishes)


if(dishes < 5):
  print("You don't have to wash the dishes. Please enjoy a tasty snack.")
elif(dishes == 10):
  print("You must wash the dishes immediately, please.")
else: 
  print("There are too many dishes, it's time to put them in the dishwasher and run it.")

"""

num0=input("Enter how much money you spent on food this week $: ")
num1=input("Enter how much money you spent on transportation this week $: ")
num2=input("Enter how much money you spent on rent this week $: ")
num3=input("Enter how much money you spent on fun activities this week $: ")
list=[int(num0), int(num1), int(num2), int(num3)]
print(list)

print(int(num0) + int(num1) + int(num2) + int(num3))

"""