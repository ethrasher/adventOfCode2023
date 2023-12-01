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
    for i in range(len(line)):
      if line[i].isnumeric():
        num += line[i]
        break
    for i in range(len(line)-1,-1,-1):
      if line[i].isnumeric():
        num+=line[i]
        break
    current += int(num)
  return current

def partB(inputLines):
  current = 0
  for line in inputLines:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    num = ""
    for i in range(len(line)):
      if line[i].isnumeric():
        num += line[i]
        break
    for i in range(len(line)-1,-1,-1):
      if line[i].isnumeric():
        num+=line[i]
        break
    current += int(num)
  return current

input = readFile("input")
# Part A Answer - 55130
print("Part A: ", partA(input))

# Part B Answer - 54985
print("Part B: ", partB(input))