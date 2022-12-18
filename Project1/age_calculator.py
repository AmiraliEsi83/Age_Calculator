# Name: Amir Ali Eslami
# My project would calculate the person's age by asking a few questions, like their name, date of birth, and educational background.
# By doing so, I would be able to determine how old the person is and what age groups they fall under.
# Next, using the inputs you provided, it will analyse your educational history.
# from datetime import date, time
import datetime


def input_taker():
    # User's name input
    Name = input("Please write down your name: ")

    # Finding the date of the birth from user
    # asking a user for three inputs
    input1 = int(input("Write down the year you were born: "))
    input2 = int(input("Write down the month you were born: "))
    input3 = int(input("Write down the day you were born: "))

    birth_date = datetime.date(input1, input2, input3)
    # today's Date
    today = datetime.date.today();
    # Difference between today's date and users date of birth
    time_difference = today - birth_date
    # finding the date of your birth in days and years and month

    age_days = time_difference.days
    age_years = (int)(age_days / 365)
    e = age_days % 365
    age_month = (int)(e / 31)


    # Printing the exact date of user's input

    print("You are", age_years, "years and", age_month, "month old")
    the_person_detail = f"This means you were born", age_days, "days ago"
    print(the_person_detail)
    return age_years


def age(age_years):
    # In here we put the person's age in the appropriate category here.
    number = (age_years)
    # different category for different user's date of birth
    # if user's age  is less than or equal to 0 then:
    if number <= 0:
        print(" You're still a baby")
    #if user's age is less than or equal to 3 then:
    elif number <= 3:
        print("You should avoid using this computer since you are a Toddler..")
    # if user's age is less than or equal to 17 then:
    elif number <= 17:
        print("You are a Teenager, so enjoy your life as much as possible because since university started, you'll need to put in the most study time possible if you want to do well.")
    # if user's age is less than or equal to 21 then:
    elif number <= 21:
        print("You are a Young Adults, pay attention to your studies and enjoy life at the sam time")
    # if user's age is less than or equal to 45 then:
    elif number <= 45:
        print("You are an Adults.")
    # if user's age is less than or equal to 120 then:
    elif number <= 120:
        print("You are an old Adults.")
    # if user's age is greater 120 then:
    else:
        print("There is no way you are so old. ")


def study(age_years):
    # asking from user about the educational background
    Study = input("which of these educational background do you have: University ,College , none : ")

    # Analysing the person educational  background
    if age_years < 18:
        # if user's input was less than 18 then we have 3 options for the educational background
        if Study == 'University':
        # if user's age was less than 18 and select Univerity then:
            print('you are still young, but you have a very bright future infront of you. ')
        else:
            # if user's age was less than 18 and select none then:
            print('You are probably still in High School and you have so much to learn in life ')
    elif age_years >= 18 and age_years < 65 and Study == 'University':
        # if user's age is greater than or equal to 18 and less than 65 with selecting University then:
        print('You are in a age that you know what are you going to do in your life')
    else:
        # if user's age is greater than or equal to 18 and less than 65 with selecting College then:
        if Study == 'College':
            print('you are still young so focus on your goal.')
        else:
            # if user's age is greater than or equal to 18 and less than 65 with selecting none then:
            print('you are probably thinking you do not any need education, but trust me its better if you do ')



if __name__ == '__main__':
    age_user = input_taker()
    age(age_user)
    study(age_user)
    