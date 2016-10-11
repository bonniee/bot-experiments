
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

def drawRect(x, y, color):
  return """
      <rect x="{0}" y="{1}" style="fill:#{2}" width="{3}" height="{4}"/>
  """.format(x, y, color, SYMBOL_WIDTH, SYMBOL_HEIGHT)

def drawCardContents(x, y, num, color):
  yOffset = y + (CARD_HEIGHT / 2.0) - (SYMBOL_HEIGHT / 2.0)
  if (num == 1):
    return drawRect(
      x + (CARD_WIDTH / 2.0) - (SYMBOL_WIDTH / 2.0),
      yOffset,
      color)
  elif (num == 2):
    return drawRect(
        x + (CARD_WIDTH / 3.0) - (SYMBOL_WIDTH / 2.0),
        yOffset,
        color
      ) + drawRect(
        x + (2 * CARD_WIDTH / 3.0) - (SYMBOL_WIDTH / 2.0),
        yOffset,
        color
      )
  else:
    return drawRect(x, y, color)

def mkCard(x, y):
  ret = """
    <rect x="{0}" y="{1}" style="fill:#FFFFFF" width="120" height="60"/>
  """.format(x, y)
  ret += drawCardContents(x, y, 2, "FF2222")
  return ret

def mkCards():
  rects = ""
  for i in range(4):
    for j in range(3):
      x = (i * 140) + 20
      y = (j * 80) + 20
      rects += mkCard(x, y)
  return rects


body += mkCards()

print prefix
print body
print suffix
