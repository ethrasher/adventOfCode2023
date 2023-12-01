def readFile(fileName):
  file1 = open(fileName + '.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return line.strip()

def partA(inputLines):
  current = 0
  for line in inputLines:
    num = ""
    i = 0
    while (not line[i].isnumeric()):
      i += 1
    num += line[i]

    i = len(line)-1
    while (not line[i].isnumeric()):
      i -= 1
    num += line[i]
    current += int(num)
  return current

def partB(inputLines):
  for i in range(len(inputLines)):
    line = inputLines[i]
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replace = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
    for j in range(len(spelled)):
      line = line.replace(spelled[j], replace[j])
    inputLines[i] = line
  return partA(inputLines)

input = readFile("input")
# Part A Answer - 55130
print("Part A: ", partA(input))

# Part B Answer - 54985
print("Part B: ", partB(input))