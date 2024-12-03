# Read input file
with open("input.txt", "r") as file:
    # Read data from file
    data = file.read().splitlines()

    # Create two lists to store values
    leftColumn = []
    rightColumn = []
    distancesList = []

    # Iterate through data and store each column in a list
    for lines in data:
        line = lines.split(" ")
        leftColumn.append(line[0])
        rightColumn.append(line[1])

    # Sort both lists in ascending order
    leftColumn.sort()
    rightColumn.sort()

    # For each line in lists find distance
    for i in range(len(leftColumn)):
        distancesList.append(abs(int(leftColumn[i]) - int(rightColumn[i])))

    # Add all the numbers in the difference list for the final answer
    answer = sum(distancesList)
    print(answer)

file.close()