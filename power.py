name = input ("hey,what is your name?")
print (name)

age = int(input ("okay,%s what is your age?" %(name)))
months= int(input("And how many months?"))
print("So %s your are %s years and %s months"%(name,age,months))


import datetime
now = datetime.datetime.now()
birth_year=(now.year - age)
print("YOU WERE BORN IN %s"%(birth_year))
years = (now.year + 100)- age
print("%s your age will be 100 years in %s "%(name,years))



print("This information was provided on :/n")
print(now)