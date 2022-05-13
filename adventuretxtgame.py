import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("You enter a house and the door locks suddenly.")
    print_pause("There's no turning back now!")
    print_pause("The only exit is the back door.\n")
    print_pause("You must go through the house to exit.")
    print_pause("There are few obstacles along the way.\n"
                "So choose wisely!\n")


def first_room(items, health):
    print_pause("You've noticed there are two doors to open.")
    print_pause("One on the left and one on the right.")
    response = valid_input("Which door would you like to open? "
                           "left or the right?\n"
                           "Please type 'r' for right or 'l' for left.\n",
                           "r", "l")
    if response == "r":
        print_pause("You have chosen to open the door to the right.")
        second_room(items, health)
    elif response == "l":
        print_pause("You have chosen to open the door on the left.")
        second_room(items, health)


def second_room(items, health):
    print_pause("You have entered the living room.\n")
    print_pause("While you're walking, you see a " + items + " on the floor.")
    response = valid_input("Do you want to collect it" + " "
                           "for later use as protection?\n"
                           "Type 'yes' or 'no'.\n",
                           "yes", "no")
    health = 100
    if response == "no":
        print_pause("That's okay, you still have other\n"
                    "items to use for protection.")
        monster_attack(items, health)
    elif response == "yes":
        print_pause("You have collected the item.")
        print(f"Your health is at {health} %.")
        monster_attack(items, health)


def monster_attack(items, health):
    print_pause("You've entered a dark room. "
                "You hear the sounds of a monster.\n")
    print_pause("As the monster approaches you, the sounds get louder.")
    response = valid_input("Would you like to fight or flee?\n"
                           "Type 'fight' or 'flee' below.\n",
                           "fight", "flee")
    if response == "flee":
        print_pause("You were able to escape without being harmed.")
        third_room(items, health)
    elif response == "fight":
        print_pause(f"You've use a {items} to defend yourself in this attack.")
        print_pause("You were able to defeat your opponent.")
        print_pause("The monster knocked you into a wall.\n"
                    "Sadly, this lowered your health.")
        health -= 20
        print_pause(f"You have {health} % health left.")
        third_room(items, health)


def third_room(items, health):
    print_pause("You have entered dining room.")
    print_pause("You noticed there is an alien that is ready to attack.")
    response = valid_input("Would you like to fight or flee?\n"
                           "Type 'fight' or 'flee' below.\n",
                           "fight", "flee")
    if response == "flee":
        print_pause("You have been defeated.\n"
                    "Unfortunately you've died! Game over!")
        play_again(items, health)
    elif response == "fight":
        print_pause(f"You've use a {items} to defend yourself in this attack.")
        print_pause("You've beat the alien," + " "
                    "but the alien stepped on your toe.\n"
                    "Sadly, this lowered your health.")
        health -= 15
        print_pause(f"You have {health} % of health left.")
        fourth_room(items, health)
    return health


def fourth_room(items, health):
    print_pause("You entered the kitchen."
                "The kitchen light is very dim.")
    print_pause("You turn on the kitchen light to see and you've noticed\n"
                "a group of bats that are ready to attack.")
    response = valid_input("Would you like to fight or flee?\n"
                           "Type 'fight' or 'flee' below.\n",
                           "fight", "flee")
    if response == "flee":
        print_pause("You were out-numbered by the bats and unfortunately\n"
                    "you ran out of health. Game over!")
        play_again(items, health)
    elif response == "fight":
        print_pause(f"You use a {items} to defend yourself.")
        health = health - random.randint(40, 65)
        print_pause(f"You have {health} % health left.")
        end_game(items, health)


def end_game(items, health):
    if health <= 35:
        print("Unfortunately, you have died! Game over.")
        play_again(items, health)
    elif health >= 36:
        print_pause("The bats ran away and you were" + " "
                    "able to escape the house.\n"
                    "You've won!")
        play_again(items, health)


def play_again(items, health):
    response = valid_input("Would you like to play again? yes or no?\n",
                           "yes", "no")
    if response == "no":
        print("Okay, Goodbye!")
        exit()
    elif response == "yes":
        print_pause("Okay, Good!")
        first_room(items, health)


def play_game():
    health = 100
    items = random.choice(["rock", "shield", "sword"])
    intro()
    first_room(items, health)
    second_room(items, health)
    monster_attack(items, health)
    third_room(items, health)
    fourth_room(items, health)
    end_game(items, health)
    play_again(items, health)


play_game()
