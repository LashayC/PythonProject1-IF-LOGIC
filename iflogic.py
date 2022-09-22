#!/usr/bin/env python3
""" If Logic quiz that finds out what disney villain you are"""

def main():

    # set evil rating counter. Quiz answers sum range is 3-9
    evil_rating = 0

    # set villain variable
    disney_villain = ""

    # function to tally evil rating. Quiz answers sum range is 3-9
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
            print("new res " + res)
        return res

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

    # create list of villains
    disney_villain_list = ["Captain Hook of 'Peter Pan'", "Maleficient of 'Sleeping Beauty'", "Gaston 'Beauty and the Beast'", "Ursula of 'The Little Mermaid'", "Mother Gothel of 'Rapunzel'", "Scar of 'The Lion King'", "Randall Boggs of 'Monsters Inc'"]

    # print which villain based on evil_rating - 3 for indexing.
    print(f"On the disney villain scale your rating is {disney_villain_list[evil_rating - 3]}")

##possible: add and print summary of each villain
##dictionary: key is villain name, value is summary?
##create function that gets villain based on evil_rating
##create dictionary, key is the evil_rating: value is list [villain name, villain summary]
##condense each quiz question into single function whose parameter is a list of input questions that'll run one by one

#calls main
if __name__ == "__main__":
    main()