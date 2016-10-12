
prefix = """
<svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="580" height="260">
"""

suffix = """
</svg>
"""

body="""
  <rect x="0" y="0" style="fill:#FFBBBB" width="580" height="260"/>
"""

CARD_HEIGHT = 60
CARD_WIDTH = 120

SYMBOL_HEIGHT = 20
SYMBOL_WIDTH = 20
CARD_MARGIN = 20

HATCHING = """<pattern id="diagonalHatch" width="10" height="10" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="10" style="stroke:black; stroke-width:1" />
</pattern>"""

prefix += HATCHING

def drawRect(x, y, color):
  return """
      <rect x="{0}" y="{1}" style="fill:#{2}" width="{3}" height="{4}"/>
  """.format(x, y, color, SYMBOL_WIDTH, SYMBOL_HEIGHT)

def drawCircle(x, y, color):
  r = SYMBOL_WIDTH / 2.0
  cx = r + x
  cy = r + y
  return """
      <ellipse cx="{0}" cy="{1}" style="fill:#{2}" rx="{3}" ry="{3}"/>
  """.format(cx, cy, color, r)

def drawTriangle(x, y, color):
  r = SYMBOL_WIDTH / 2.0
  return """<polygon points="{} {}, {} {}, {} {}" style="fill:#{}"/>
  """.format(x + r, y, x + SYMBOL_WIDTH, y + SYMBOL_HEIGHT, x, y + SYMBOL_HEIGHT, color)



def drawCardContents(x, y, num, color):
  yOffset = y + (CARD_HEIGHT / 2.0) - (SYMBOL_HEIGHT / 2.0)
  xInterval = CARD_WIDTH / float(num + 1.0)
  xMargin = SYMBOL_WIDTH / 2.0

  coords = [(x + ((1 + i) * xInterval) - xMargin, yOffset) for i in range(num)]

  ret = ""
  for (a, b) in coords:
    ret += drawTriangle(a, b, color)

  return ret

def mkCard(x, y):
  ret = """
    <rect x="{0}" y="{1}" style="fill:#FFFFFF" width="120" height="60"/>
  """.format(x, y)
  ret += drawCardContents(x, y, 3, "FF2222")
  return ret

def mkCards():
  rects = ""
  for i in range(4):
    for j in range(3):
      x = (i * (CARD_WIDTH + CARD_MARGIN)) + CARD_MARGIN
      y = (j * (CARD_HEIGHT + CARD_MARGIN)) + CARD_MARGIN
      rects += mkCard(x, y)
  return rects

body += mkCards()

print prefix
print body
print suffix
