# Read input file
with open("input.txt", "r") as file:
    # Read data from file
    data = file.read().splitlines()

    # Create two lists to store values
    leftColumn = []
    rightColumn = []
    occurrenceList = []

    # Iterate through data and store each column in a list
    for lines in data:
        line = lines.split(" ")
        leftColumn.append(line[0])
        rightColumn.append(line[1])

    # For each item in left list:
    # - count how many times it appears in the right list;
    # - multiply the item from the left by the count from step 1
    # - add final number to a list
    for i in range(len(rightColumn)):
        occurrenceList.append(abs(int(leftColumn[i]) * int(rightColumn.count(leftColumn[i]))))

    # Sum up all the occurrences for the final answer
    answer = sum(occurrenceList)

file.close()