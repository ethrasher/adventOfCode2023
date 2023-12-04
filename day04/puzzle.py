def readFile(fileName):
  file1 = open(fileName + '.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  line = line.split(": ")[1].strip()
  winningNums,haveNums = line.split(" | ")
  winningNums = winningNums.replace("  ", " ").strip().split(" ")
  winningNums = list(map(lambda x: int(x), winningNums))
  haveNums = haveNums.replace("  ", " ").strip().split(" ")
  haveNums = list(map(lambda x: int(x), haveNums))
  return {"winningNums": set(winningNums), "haveNums": set(haveNums)}

def getPointsForCard(card):
  count = 0
  for num in card["haveNums"]:
    if num in card["winningNums"]:
      count += 1
  return count


def partA(inputLines):
  total = 0
  for card in inputLines:
    count = getPointsForCard(card)
    if count > 0:
      total += 2**(count-1)
  return total
      

def partB(inputLines):
  totalCards = [1 for card in inputLines]
  for i in range(len(inputLines)):
    card = inputLines[i]
    count = getPointsForCard(card)
    for j in range(1,count+1):
      if i+j < len(totalCards):
        totalCards[i+j] += totalCards[i]
  return sum(totalCards)


input = readFile("input")
# Part A Answer - 27845
print("Part A: ", partA(input))

# Part B Answer - 9496801
print("Part B: ", partB(input))