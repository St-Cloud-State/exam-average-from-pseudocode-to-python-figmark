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
#Define the function
def calculate_average():
# Prompt user to enter first score as integer
    first_score = int(input("Enter first exam score: "))
# Prompt user to enter second score as integer
    second_score = int(input("Enter second exam score: "))
# Prompt user to enter third score as integer
    third_score = int(input("Enter third exam score: "))
# Calculate the average score
    average_score = (first_score + second_score + third_score) / 3
# Print first score back for user to see
    print("First score:", first_score)
# Print second score back for user to see
    print("Second score:", second_score)
# Print third score back for user to see
    print("Third score:", third_score)
# Print the average score
    print("The average score is:", average_score)
# Call the function
calculate_average()