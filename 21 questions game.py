
secret_word = "animal crossing"
guess = ""
guess_count = 0
guess_limit = 21

out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = input("Enter a guess: ")
        if guess == secret_word:
            break
    if guess_count == 1:

        print("its a thing")
        print("you have "+ str( guess_limit - guess_count) + " guesses left!")


        continue
    if guess_count ==2:
        print("its a thing you like")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")

        continue
    if guess_count == 3:
        print("you can buy this")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 4:
        print("you talk about it pretty often")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 5:
        print("i cant stand it")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 6:
        print("i hate the stupid sounds they make")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 7:
        print("is it really taking you this long?")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 8:
        print("everyone has this")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 9:
        print("i hate this game")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 10:
        print("its about $59")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 11:
        print("stupid little cute animals")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 12:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 13:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 14:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 15:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 16:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 17:
        print("its not a human")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 18:
        print("this thing takes up alot of time")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 19:
        print("this is number 19")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 20:
        print("this is number 20")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue
    if guess_count == 21:
        print("its a video game")
        print("you have " + str(guess_limit - guess_count) + " guesses left!")
        continue


    else:
        out_of_guesses = True

if out_of_guesses:
    print("its animal crossing!!!! you lose!!")
else:
    print("You win!")