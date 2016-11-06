"""
Generate some number of SET boards
and print them in Tracery format,
for submission to Cheap Bots Done Quick.
"""

from board import drawBoard
from random import sample

plainQuote = '"'
escapedQuote = "\\\""

plainHash = '#'
escapedHash = "\\\\#"


def tracerySVG(svg):
  return svg.replace(plainQuote, escapedQuote).replace(plainHash, escapedHash)

def tracery(svgs):
  j = """
  {
    "origin": [ """
  for svg in svgs:
    j += ' "{svg '
    j += svg.strip().replace('\n', '')
    j += '}",'
  j = j[:-1]
  j += "] }"
  return j

cards = []
for shape in range(3):
  for color in range(3):
    for number in range(1, 4):
      for pattern in range(3):
        cards.append({"color": color, "shape": shape, "number": number, "pattern": pattern})

hand = sample(cards, 12)
boardSVG = drawBoard(hand)

svgs = [tracerySVG(drawBoard(sample(cards, 12))) for i in range(50)]

print tracery(svgs)