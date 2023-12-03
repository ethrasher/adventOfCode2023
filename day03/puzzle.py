def readFile(fileName):
  file1 = open(fileName + '.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return list(line.strip())


  
    
  
def partA(inputLines):
  total = 0
  curNum = ''
  curNumTouchingSymbol = False
  for row in range(len(inputLines)):
    for col in range(len(inputLines[0])):
      if not inputLines[row][col].isnumeric():
        if curNum != '':
          if curNumTouchingSymbol:
            total += int(curNum)
            curNumTouchingSymbol = False
          curNum = ''
      else:
        curNum += inputLines[row][col]
        if not curNumTouchingSymbol:
          dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
          for dir in dirs:
            checkRow,checkCol = row+dir[0],col+dir[1]
            if checkRow >= 0 and checkRow < len(inputLines) and checkCol >= 0 and checkCol < len(inputLines[0]):
              if not inputLines[checkRow][checkCol].isnumeric() and inputLines[checkRow][checkCol] != '.':
                curNumTouchingSymbol = True
    # end of row
    if curNum != '':
      if curNumTouchingSymbol:
        total += int(curNum)
        curNumTouchingSymbol = None
      curNum = ''
  return total     

def getNumFromStartPosition(inputLines, row, col):
  fullNum = inputLines[row][col]
  foundNumPositions = set()
  foundNumPositions.add((row,col))
  curCol = col-1
  while curCol >= 0 and inputLines[row][curCol].isnumeric():
    fullNum = inputLines[row][curCol] + fullNum
    foundNumPositions.add((row, curCol))
    curCol = curCol-1
    
  curCol = col+1
  while curCol < len(inputLines[0]) and inputLines[row][curCol].isnumeric():
    fullNum += inputLines[row][curCol]
    foundNumPositions.add((row, curCol))
    curCol = curCol+1
  return int(fullNum), foundNumPositions

def findAdjacentNums(inputLines, row, col):
  seen = set()
  dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  result = []
  for dir in dirs:
    checkRow,checkCol = row+dir[0],col+dir[1]
    if (checkRow >= 0 and 
        checkRow < len(inputLines) and 
        checkCol >= 0 and 
        checkCol < len(inputLines[0]) and 
        (checkRow,checkCol) not in seen and
        inputLines[checkRow][checkCol].isnumeric()):
      num, positions = getNumFromStartPosition(inputLines, checkRow,checkCol)
      result.append(num)
      seen = seen.union(positions)
  return result

def partB(inputLines):
  total = 0 
  for row in range(len(inputLines)):
    for col in range(len(inputLines[0])):
      if inputLines[row][col] == "*":
        adjacentNums = findAdjacentNums(inputLines, row, col)
        if len(adjacentNums) == 2:
          gearRatio = adjacentNums[0]*adjacentNums[1]
          total += gearRatio
  return total

input = readFile("input")
# Part A Answer - 538046
print("Part A: ", partA(input))

# Part B Answer - 81709807
print("Part B: ", partB(input))