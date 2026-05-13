# Average Score Calculator

try:
    score1 = float(input("Enter first score: "))
    score2 = float(input("Enter second score: "))
    score3 = float(input("Enter third score: "))

    average = (score1 + score2 + score3) / 3

    print("\nTest Scores")
    print("First Score:", score1)
    print("Second Score:", score2)
    print("Third Score:", score3)

    print("Average Score:", average)

except ValueError:
    print("Invalid input! Please enter numbers only.")
