# Your friend will complete this function
def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    if result == -1:
        print("I win!")
    elif result == 1:
        print("You win!")
    elif result == 0:
        print("Game drawn!")
    print("Human plays first={0}, winner={1} "
          .format(human_plays_first, result))
    again = input("Do you want to play again: ")
    while again == "Yes":
        if result == -1:
            print("I win!")
        elif result == 1:
            print("You win!")
        elif result == 0:
            print("Game drawn!")
        while again == "No":
            print("Goodbye!")
    return result

play_once(True)