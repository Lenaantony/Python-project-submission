score = 0


def argentina():
    global score

    print("\n=== ARGENTINA ===")
    print("You arrive in Buenos Aires.")
    print("Where will you investigate?")
    print("1. AFA Football Museum")
    print("2. La Bombonera Stadium")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nYou find a hidden note inside the museum.")
        print("'Follow the city of samba.'")
        print("+10 Score")
        score += 10
    else:
        print("\nThe clue was fake.")
        print("-5 Score")
        score -= 5


def brazil():
    global score

    print("\n=== BRAZIL ===")
    print("You arrive in Rio de Janeiro.")
    print("Where will you investigate?")
    print("1. Maracana Stadium")
    print("2. Abandoned Harbor Warehouse")

    choice = input("Enter choice: ")

    if choice == "2":
        print("\nYou discover security footage.")
        print("The thief boarded a jet to Portugal.")
        print("+10 Score")
        score += 10
    else:
        print("\nNothing useful is found.")
        print("-5 Score")
        score -= 5


def portugal():
    global score

    print("\n=== PORTUGAL ===")
    print("You arrive in Lisbon.")
    print("Where will you investigate?")
    print("1. Football Hall of Fame")
    print("2. Lisbon Docks")

    choice = input("Enter choice: ")

    if choice == "2":
        print("\nYou find a shipping manifest.")
        print("The trophy has been moved to Paris.")
        print("+10 Score")
        score += 10
    else:
        print("\nThe trail goes cold.")
        print("-5 Score")
        score -= 5


def france():
    global score

    print("\n=== FRANCE ===")
    print("You arrive in Paris.")
    print("Where will you investigate?")
    print("1. Louvre Museum")
    print("2. Underground Metro Station")

    choice = input("Enter choice: ")

    if choice == "2":
        print("\nYou find the final clue.")
        print("'Return to MetLife Stadium.'")
        print("+10 Score")
        score += 10
    else:
        print("\nIt was a distraction.")
        print("-5 Score")
        score -= 5


def final_mission():
    global score

    print("\n=== FINAL MISSION ===")
    print("You return to MetLife Stadium.")
    print("A mysterious groundskeeper approaches.")
    print("'I know where the trophy is.'")

    print("\n1. Trust the groundskeeper")
    print("2. Follow your clues")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nBAD ENDING")
        print("The groundskeeper was working with the thieves.")
        print("The trophy disappears forever.")
        print("The World Cup begins without its trophy.")
    else:
        if score >= 30:
            print("\nPERFECT ENDING")
            print("You use the clues collected across four countries.")
            print("You discover a hidden tunnel beneath the stadium.")
            print("The World Cup Trophy is recovered!")
            print("The thieves are arrested.")
            print("You saved the World Cup!")
        else:
            print("\nGOOD ENDING")
            print("You eventually locate the trophy.")
            print("The opening ceremony is delayed,")
            print("but the tournament is saved.")


def game():
    global score

    print("=" * 50)
    print("THE LOST WORLD CUP TROPHY")
    print("=" * 50)

    player_name = input("Enter your name: ")

    print(f"\nWelcome Detective {player_name}!")

    print("""
June 10, 2026
MetLife Stadium, New Jersey

Hours before the opening ceremony,
the FIFA World Cup Trophy has been stolen.

A mysterious envelope contains clues
leading across the football world.

Your mission is to recover the trophy
before the tournament begins.
""")

    input("\nPress Enter to begin your investigation...")

    argentina()
    brazil()
    portugal()
    france()

    print("\nCurrent Score:", score)

    final_mission()

    print("\nFinal Score:", score)
    print("\nThank you for playing!")


game()