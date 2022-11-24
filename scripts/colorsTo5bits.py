colors = [0x28a745ff, 0xfd7e14ff, 0xb42b6fff, 0x560dcbff]

# convert r, g, and b values to 5 bits
def to5bits(color):
  # remove alpha channel
  color >>= 8
  b = color & 0xff
  g = (color >> 8) & 0xff
  r = (color >> 16) & 0xff

  print(f"RGB15({r >> 3}, {g>>3}, {b>>3})")

for color in colors:
  to5bits(color)
