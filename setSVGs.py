import itertools
from random import shuffle, sample

cards = []
for shape in range(3):
  for color in range(3):
    for number in range(1, 4):
      for pattern in range(3):
        cards.append({"color": color, "shape": shape, "number": number, "pattern": pattern})
# print cards

# for i in range(4):
#   shuffle(cards)
#   print itertools.combinations(cards, 12).next()

# board = itertools.combinations(cards, 12).next()
board = sample(cards, 12)

prefix = """
<svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="580" height="260">
"""

suffix = """
</svg>
"""

body="""
  <rect x="0" y="0" style="fill:#e8efed" width="580" height="260"/>
"""

CARD_HEIGHT = 60
CARD_WIDTH = 120

SYMBOL_HEIGHT = 20
SYMBOL_WIDTH = 20
CARD_MARGIN = 20

STROKE_WIDTH = SYMBOL_WIDTH / 5.0

COLORS = ["66c2a5", "fc8d62", "8da0cb"]

HATCHING = """
<pattern id="hatch{0}" width="4" height="4" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
<ellipse cx="2" cy="2" rx="1.3" ry="1.3" fill="#{0}"/>
</pattern>
"""

for c in COLORS:
  prefix += HATCHING.format(c)


def drawRect(x, y, style):
  return """
      <rect x="{}" y="{}" width="{}" height="{}" {}/>
  """.format(x, y, SYMBOL_WIDTH, SYMBOL_HEIGHT, style)

def drawCircle(x, y, style):
  r = SYMBOL_WIDTH / 2.0
  cx = r + x
  cy = r + y
  return """
      <ellipse cx="{}" cy="{}" rx="{}" ry="{}" {}/>
  """.format(cx, cy, r, r, style)

def drawTriangle(x, y, style):
  r = SYMBOL_WIDTH / 2.0
  return """<polygon points="{} {}, {} {}, {} {}" {}/>
  """.format(x + r, y, x + SYMBOL_WIDTH, y + SYMBOL_HEIGHT, x, y + SYMBOL_HEIGHT, style)

def style(pattern, color):
  styleString = """stroke="#{}" stroke-width="5"
  """.format(color)

  if (pattern == 0):
    # Solid
    styleString += """
      fill="#{}"
    """.format(color)
  elif (pattern == 1):
    # Hollow
    styleString += """
      fill="transparent"
    """
  else:
    # Striped
    styleString += """
    fill="url(#hatch{})" 
    """.format(color)

  return styleString

def drawCardContents(x, y, num, color, shape, pattern):
  yOffset = y + (CARD_HEIGHT / 2.0) - (SYMBOL_HEIGHT / 2.0)
  xInterval = CARD_WIDTH / float(num + 1.0)
  xMargin = SYMBOL_WIDTH / 2.0

  colorCode = "66c2a5"
  if (color == 1):
    colorCode = "fc8d62"
  elif (color == 2):
    colorCode = "8da0cb"

  coords = [(x + ((1 + i) * xInterval) - xMargin, yOffset) for i in range(num)]
  styleString = style(pattern, colorCode)

  ret = ""
  for (a, b) in coords:
    if (shape == 0):
      ret += drawRect(a, b, styleString)
    elif (shape == 1):
      ret += drawCircle(a, b, styleString)
    else:
      ret += drawTriangle(a, b, styleString)

  return ret

def mkCard(x, y):
  ret = """
    <rect x="{0}" y="{1}" rx="5" ry="5" style="fill:#FFFFFF" width="120" height="60"/>
  """.format(x, y)
  # ret += drawCardContents(x, y, 3, "FF2222")
  return ret

def mkCards():
  rects = ""
  for i in range(4):
    for j in range(3):
      x = (i * (CARD_WIDTH + CARD_MARGIN)) + CARD_MARGIN
      y = (j * (CARD_HEIGHT + CARD_MARGIN)) + CARD_MARGIN
      rects += mkCard(x, y)

      card = board[(i * 3) + j]
      rects += drawCardContents(x, y, card["number"], card["color"], card["shape"], card["pattern"])

  return rects

body += mkCards()

print prefix
print body
print suffix



