name = input("Type Your name: ")
print(f"Welcome {name} to this adventure!")


answer = input("You are on a dirt road, it has come ton an end and you can go (left/right). Which hway would you like to go? ")

if answer == "left":

    answer = input("You come to a river🌄 You can walk around it or swim🌊 accross? type walk to (walk🚶‍♂️/swim🤽‍♀️) accross: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.🙋")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game.👷‍♂️")
    else:
        print("Not a valid option. You lose👊")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You Go back. You lose")
    elif answer == "cross":
        answer = input("You cross the bridege and meet a stranger. Do you talk to them👀: ")

        if answer == "yes":
            print("You talk to the stanger and tehy give you gold🔶. You Win!🥳")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose🖐️")
        else:
            print("Not a valid option. You lose.👊")
    else:
        print("Not a valid option. You lose👊")

else:
    print("Not a valid option. You lose👊")