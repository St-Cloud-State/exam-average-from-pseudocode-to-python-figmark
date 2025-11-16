"""
Marcus Walker
IS250-01
Files and Exceptions Project Setup
11-16-2025
"""
"""
Pseudocode
1. Define my function which I will call average_calculator.
2. Prompt the user to enter first exam score as an integer.
3. Prompt the user to enter second exam score as an integer.
4. Prompt the user to enter third exam score as an integer.
5. Compute the average by adding them together and dividing by three.
6. Print the scores individually on their own lines.
7. Print the final average score on its own line.
8. End the program.
"""

def calculate_average():
    first_score = int(input("Enter first exam score: "))
    second_score = int(input("Enter second exam score: "))
    third_score = int(input("Enter third exam score: "))
    average_score = (first_score + second_score + third_score) / 3
    print("First score:", first_score)
    print("Second score:", second_score)
    print("Third score:", third_score)
    print("The average score is:", average_score)
calculate_average()

