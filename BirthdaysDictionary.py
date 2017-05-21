import time
birthdays = {
  "Albert Einstein":"14/3/1889",
  "Bill Gates":"28/10/1955",
  "Steve Jobs":"24/2/1955",
}
print("Welcome to the birthday game ! We have the birthdays to:")
time.sleep(1)
for x in birthdays:
  print(x)
  time.sleep(0.7)
choice = input("\nWho's birthday do you want to look up?")

if choice in birthdays:
  print("The birthday of {} is:".format(choice))
  print(birthdays[choice])
