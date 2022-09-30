#!/usr/bin/env python3
""" If Logic quiz that finds out what disney villain you are"""

    # function to tally evil rating. Quiz answers sum range is 3-9
import re


def villain_quiz_calculator(letter):
    if letter == "a":
        return 1
    elif letter == "b":
        return 2
    elif letter == "c": 
        return 3
    else:
        print("Invalid argument for letter")

# function checking for valid responses
def valid_response_chk(res):
    res = res.lower()
    if res == "a" or res == "b" or res == "c":
        return res
    while res != "a" and res != "b" and res != "c":
        res = input("Please choose from given options: ").lower()
    return res

# function for assigning villain
def assign_villain(rating):
    if rating == 3:
        return "Captain Hook"
    elif rating == 4:
        return "Maleficient"
    elif rating == 5:
        return "Gaston"
    elif rating == 6:
        return "Ursula"
    elif rating == 7:
        return "Mother Gothel"
    elif rating == 8:
        return "Scar"
    elif rating == 9:
        return "Randall"

def main():
    # set evil rating counter. Quiz answers sum range is 3-9
    evil_rating = 0

    # print explaining the quiz
    print("Find out what disney villain you are on the evil scale by answering the questions below!")

    # conditional to get and save quiz answers
    response = input("Someone leaves a 5-star lunch in the breakroom, what do you do? \n a. Take it and hide to eat it. \n b. Take it, eat with everyone, then leave it on another's desk. \n c. Take it, eat it, and put the empty container back where you found it. \n Answer: ")
    response = valid_response_chk(response)
    evil_rating += villain_quiz_calculator(response)

    # input for second quiz question
    response = input("Sharing is caring! You're told to share your games by an authority figure. What do you do? \n a. Negotiate for their best game. \n b. Pretend to share, then take it back when no one's looking. \n c. Break your game, hand it over, and pretend the other person broke it. \n Answer: ")
    response = valid_response_chk(response)
    evil_rating += villain_quiz_calculator(response)

    # input for second quiz question
    response = input("You let someone borrow a pen, they never return it. What do you do? \n a. Take one of their pens. \n b. Take their entire pen cup. \n c. Take their entire pen cup and and trash it. \n Answer: ")
    response = valid_response_chk(response)
    evil_rating += villain_quiz_calculator(response)

    # dictionary with villain rating, name, and description
    villain_dict = {
        "Captain Hook" : {
            "movie" : "Peter Pan",
            "rating" : "Number 7 of 7",
            "summary" : "You are only trying to make right what was wrong. I mean, you're the one missing an arm! You don't go out looking for trouble per se, but if it comes you're way you're going to see it through!"
        },
        "Maleficient" : {
            "movie" : "Sleeping Beauty",
            "rating" : "Number 6 of 7",
            "summary": "Every so often you cause a little mischief, but thats no reason not to invite you to the party! Afterall, malice is just a another word. Only when you're scorned is when the real claws come out."
        },
        "Gaston" : {
            "movie" : "Beauty & the Beast",
            "rating" : "Number 5 of 7",
            "summary" : "In your defense, you did think the beast was the villain at first. After that it was all you. Manipulating the story to fit your narrative is an art you've got down pat. Afterall, no one incites a murderous mob like Gaston!"
        },
        "Ursula" : {
            "movie" : "The Little Mermaid",
            "rating" : "Number 4 of 7", 
            "summary" : "You are first and foremost, a business. They sign the contract and the terms are clear as day! Now if you decide to mettle a bit the change the odds, its the signers fault for not thinking ahead! It's all about the bottom line."
        },
        "Mother Gothel" : {
            "movie" : "Rapunzel",
            "rating" : "Number 3 of 7",
            "summary" : "Now, rapunzel was well taken care of in that tower. To say that the goal was a lifetime of imprisonment is a total exagerration. But if it wasn't, its the least she can do for your eternal youth. When it comes to getting what you want, nothing is off the table."
        },
        "Scar" : {
            "movie" : "The Lion King",
            "rating" : "Number 2 of 7",
            "summary" : "Ruthless, thy name is Scar. In pursuit of power, there's nothing you wouldn't do? And why should you hesitate, everything you see is already your's its just a matter of taking it!"
        },
        "Randall" : {
            "movie" : "Monsters Inc.",
            "rating" : "Number 1 of 7",
            "summary" : "You would have been number 1! Just as long as those other 2 monsters stayed out of the way. Workplace fraud, manipulation, and overall unpleasantness have brought you to first place. Someone once said there are those who just wanna watch the world burn and you are dancing in the flames!"
        }
    }

    # set villain variable
    villain = assign_villain(evil_rating)

    # print villain variable
    print(f"""
    The disney villain you are is {villain} of {villain_dict[villain]['movie']}. 
    You have the rating {villain_dict[villain]['rating']}. 
    Summary: {villain_dict[villain]['summary']}
    """)


#calls main
if __name__ == "__main__":
    main()