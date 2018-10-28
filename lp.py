choice = raw_input('Enjoying the course? (y/n)')
if choice == "y":
  print "welcome"
  else:
   print "sorry"
while choice != "y"and choice != "n":  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
