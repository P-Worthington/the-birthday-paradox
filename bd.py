import random 

from const import dateTable

def welcome ():
    print("Welcome to Birthday Paradox")

def numberPeople ():
    while True:
        print("How many people? (Min 2 Max 100)")
        x = input("\n")
        try: 
            y = int(x)
            if y >= 2 and y <= 100:
                return y
                break
            else:
                print("Please provide valid input")
        except:
            print("Please provide valid input")


def generateBirthdays (x):
    birthdays = []
    i = 0 
    while i < x:
        date = random.randint(1, 365)
        birthdays.append(date)
        i += 1
    return birthdays

def duplicateAssessment(birthdays, x):
    duplicates = []
    for date in birthdays:
        if birthdays.count(date) > 1:
            duplicates.append(date)

    try:
        length = duplicates[-1]
        if length > 0:
            print(f'There are {length} duplicate birthdays in this gorup of {x} people')
    except:
        print(f"There are no duplicate birthdays in this gorup of {x} people")

def largeIteration(x):
    positive = 0
    i = 0
    while i < 100000:
        birthdays = generateBirthdays(x)
        for date in birthdays:
            if birthdays.count(date) > 1:
                positive += 1
        i += 1
    
    percentage = percentageMaker(positive, 100000)
    print(f'In a group of {x} people 100_000 times there are prepeat birthdays {percentage}% number of times')

def percentageMaker (result, total):
    return (result / total) *100

def main ():
    welcome()
    x = numberPeople()
    birthdays = generateBirthdays(x)
    duplicateAssessment(birthdays, x)
    print(f"Performing 100_000 iterations of {x} people and providing the percentage of times a dupliate was found")
    largeIteration(x)

main()



