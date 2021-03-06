from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # Universal truths about the game
    Biconditional(AKnight, Not(AKnave)),    # If A is a knight then A is not a knave and vice-versa
    Biconditional(BKnight, Not(BKnave)),    # If B is a knight then B is not a knave and vice-versa
    Biconditional(CKnight, Not(CKnave)),    # If C is a knight then C is not a knave and vice-versa

    # Statements saod by the characters
    Biconditional(And(AKnight, AKnave), AKnight)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # Universal truths about the game
    Biconditional(AKnight, Not(AKnave)),    # If A is a knight then A is not a knave and vice-versa
    Biconditional(BKnight, Not(BKnave)),    # If B is a knight then B is not a knave and vice-versa
    Biconditional(CKnight, Not(CKnave)),    # If C is a knight then C is not a knave and vice-versa

    # Statements saod by the characters
    Biconditional(And(AKnave, BKnave), AKnight)     # If left clause is true then character is a knight
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # Universal truths about the game
    Biconditional(AKnight, Not(AKnave)),    # If A is a knight then A is not a knave and vice-versa
    Biconditional(BKnight, Not(BKnave)),    # If B is a knight then B is not a knave and vice-versa
    Biconditional(CKnight, Not(CKnave)),    # If C is a knight then C is not a knave and vice-versa

    # Statements saod by the characters
    Biconditional(Or(And(AKnight, BKnight), And(AKnave, BKnave)), AKnight),     # If left clause is true then character is a knight
    Biconditional(Or(And(AKnight, BKnave), And(AKnave, BKnight)), BKnight)     # If left clause is true then character is a knight
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # Universal truths about the game
    Biconditional(AKnight, Not(AKnave)),    # If A is a knight then A is not a knave and vice-versa
    Biconditional(BKnight, Not(BKnave)),    # If B is a knight then B is not a knave and vice-versa
    Biconditional(CKnight, Not(CKnave)),    # If C is a knight then C is not a knave and vice-versa

    # Statements saod by the characters
    Biconditional(Or(AKnight, AKnave), AKnight),     # If left clause is true then character is a knight
    Biconditional(AKnave, BKnight),     # If left clause is true then character is a knight
    Biconditional(CKnave, BKnight),     # If left clause is true then character is a knight
    Biconditional(AKnight, CKnight)     # If left clause is true then character is a knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
