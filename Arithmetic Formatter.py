def arithmetic_arranger(problems):
    output = []
    if len(problems) > 5:
      return "Error: Too many problems."
    for problem in problems:
      problemArray = problem.split()
      maxLength = len(max(problemArray, key=len)) + 2
      if problemArray[1] == "*" or problemArray[1] == "/":
        return "Error: Operator must be '+' or '-'."
      if len(max(problemArray, key=len)) > 4:
        return "Error: Numbers cannot be more than four digits."
      if not problemArray[0].isdecimal() or not problemArray[2].isdecimal():
        return "Error: Numbers must only contain digits."
      problemString = [" "*(maxLength - len(problemArray[0])) + problemArray[0], problemArray[1] + " "*(maxLength - len(problemArray[2]) - 1) + problemArray[2], "-" * maxLength]
      output.append(problemString)
    lineOne = ""
    lineTwo = ""
    lineThree = ""
    for index in range(len(output)):
      lineOne += output[index][0] + " "*4 
      lineTwo += output[index][1] + " "*4 
      lineThree += output[index][2] + " "*4 
    return lineOne[:-4] + "\n" + lineTwo[:-4] + "\n" + lineThree[:-4]