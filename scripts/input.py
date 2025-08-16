# A python program using the input function 
print()
print()
print("---------------")

print("  ----------")
print(" |  INPUT  |")
print(" |FUNCTIONS|")
print("  ----------")

print("---------------")
print()

print("What is your name? ")
name=input()
print("Hello,",name)
print("------------", "\n")

print("Where were you born? ")
birthplace=input()
print("------------", "\n")

print("How old are you? ")
age=input()
print()
dob = 2025 - int(age)
print("Ah, ok. You were born in",dob,"\n")
print("------------", "\n")

print("Let me see if I understood you.\n")
print("Your name is ",name,
       ", and you were born in ", birthplace, " in ", dob, "\n", sep='')
print("Is that correct?")
answer=input()


if answer == ("yes" or "Yes"):
    print("I knew it!")
else: 
    print("How could I be so wrong!")