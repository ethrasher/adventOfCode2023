import copy

def readFile(fileName):
  file1 = open(fileName + '.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  game = line.strip()
  fullGameStartIndex = game.find(": ")
  game = game[fullGameStartIndex+2:]
  rounds = game.split("; ")
  for i in range(len(rounds)):
    r = rounds[i]
    colors = {"red":0, "green":0, "blue":0}
    for pull in r.split(", "):
      (num, color) = pull.split(" ")
      colors[color] += int(num)
    rounds[i] = colors
  return rounds

def partA(games):
  totalImpossible = 0
  for i in range(len(games)):
    for rnd in games[i]:
      if rnd["red"] > 12 or rnd["green"]>13 or rnd["blue"]>14:
        totalImpossible += (i+1)
        break
  
  return sum(range(1, len(games)+1)) - totalImpossible

def partB(games):
  def getMinimumColorsForGame(game):
    minColors = copy.copy(game[0])
    for rnd in game:
      for color in rnd.keys():
        minColors[color] = max(minColors[color], rnd[color])
    return minColors
  
  minimumColorsPossible = list(map(getMinimumColorsForGame, games))
  powers = list(map(lambda game: game["red"]*game["green"]*game["blue"], minimumColorsPossible))
  return sum(powers)
  

    

input = readFile("input")
# Part A Answer - 2285
print("Part A: ", partA(input))

# Part B Answer - 77021
print("Part B: ", partB(input))