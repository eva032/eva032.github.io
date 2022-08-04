# SAMPLE Python Code for Creating VR content and interacting in VR using AFrame.
# Last edited on July 7, 2022.
# Eva

import py_aframe as vrlc
vrlc.clear() # Create empty a-scene.

#vrlc.hello_aframe()
'''
box = vrlc.box()
vrlc.setColor(box, "magenta")
vrlc.setPosition(box, 4, 0, -7)
ball = vrlc.entity({
  "geometry": "primitive: sphere",
  "radius":1,
  "material": "color: indigo",
  "position": "6 3 -9"
  })
#vrlc.setAttrib(box, "color", "black")
vrlc.setScale(box, 0.5, 6, 0.5) # Make the magenta block into a post.
'''

#import random
# Set up an event handler for the right hand Oculus controller A button:
# Pressing it will cause a cube to appear.
#def handleRightA(event):
#  print("handleRightA was called with this event:", event)
#  box2 = vrlc.box()
#  vrlc.setColor(box2, random.choice(["green", "red", "magenta", "black", "gray"]))
#  vrlc.setPosition(box2, 6, 0, -7)

# Create the Javascript proxy for the handler and add it as an event listener.
#handleRightAProxy = makeHandler('abuttondown', 'right-hand', handleRightA)

# Set up a maze.

#The following maze uses '_' to represent having an east-west wall
# at the south side of a 1m x 1m cell, and '[' for a north-south
# wall on the west side of a cell. The letter 'L' means to have both.
# Blank means no wall wall in that cell.
maze = '''
___
_  [
L_[[
[ _[
LL_
'''

THICKNESS = 0.1  # in meters
WIDTH = 1
HEIGHT = 3

HALF_THICKNESS = THICKNESS / 2.0
HALF_WIDTH = WIDTH/2.0
HALF_HEIGHT = HEIGHT/2.0

AWAY = 10 # Initial z distance (depth) from viewer to maze entrance.


def wall(position_string, scale_string):
   '''Create a piece of wall for the maze.'''
   wall = vrlc.entity({
   "class": "collidable", # Actually should serve to BLOCK teleportation through walls.
    # but some mods to the teleport code will be needed to really fix this.
   "geometry": "primitive: box",
   "material": "src: img/aggregate-texture.jpg",
   "position": position_string,
   "scale": scale_string})
   return wall


def textMazeTo3D(txt):
  lines = txt.split("\n")[1:-1]
  print("nlines = ", len(lines))
  for z in range(len(lines)):
    print("Line ", z," has length ", len(lines[z]))
    for x in range(len(lines[z])):
      elt = lines[z][x]
      if elt in ['L', '[']:
        # A north-south wall
        position_string = str(x+HALF_THICKNESS)+" "+str(0+HALF_HEIGHT)+" "+str(z - HALF_WIDTH - AWAY)
        scale_string = str(THICKNESS)+" "+str(HEIGHT)+" "+str(WIDTH)
        w = wall(position_string, scale_string)
      if elt in ['L', '_']:
        # An west-east wall
        position_string = str(x+HALF_WIDTH)+" "+str(0+HALF_HEIGHT)+" "+str(z - HALF_THICKNESS - AWAY)
        scale_string = str(WIDTH)+" "+str(HEIGHT)+" "+str(THICKNESS)
        w = wall(position_string, scale_string)

#textMazeTo3D(maze)

#startBox = vrlc.box() # Shows the entrance to the maze.
#vrlc.setColor(startBox, "blue")
#vrlc.setPosition(startBox, 3, 0.14,  -AWAY + 4)
#vrlc.setScale(startBox, 0.3, 0.3, 0.3)

#endBox = vrlc.box() # Shows the exit from the maze.
#vrlc.setColor(endBox, "gold")
#vrlc.setPosition(endBox, 0, 0.15, -AWAY)
#vrlc.setScale(endBox, 0.3, 0.3, 0.3)

def floor():
   '''Create a floor for the maze.'''
   floor = vrlc.entity({
   "class": "collidable",
   "geometry": "primitive: plane; width: 20; height: 40;",
   "material": "src: img/cement-texture.jpg; repeat: 10 10;",
   "position": "0 0 "+str(-AWAY),
   "rotation": "40 0 0",
   "color": "gray"})
   return floor

#floor()


keys=[]
def block_instrument():
  #normal keys
  for i in range(7):
    box = vrlc.box()
    vrlc.setColor(box, "magenta")
    vrlc.setPosition(box, -9+3*i, 0.5, -27.5)
    keys.append(box)
  #sharps/flats
  for i in range(2):
    box = vrlc.box("A")
    vrlc.setColor(box, "purple")
    vrlc.setPosition(box, -7.5+3*i, 0.5, -29)
    keys.append(box)
  for i in range(3):
    box = vrlc.box()
    vrlc.setColor(box, "purple")
    vrlc.setPosition(box, 1.5+3*i, 0.5, -29)
    keys.append(box)
block_instrument()

def setNotes():
  vrlc.setNote(keys[0],"C")
  vrlc.setNote(keys[1],"C#")
  vrlc.setNote(keys[2],"D")
  vrlc.setNote(keys[3],"D#")
  vrlc.setNote(keys[4],"E")
  vrlc.setNote(keys[5],"F")
  vrlc.setNote(keys[6],"F#")
  vrlc.setNote(keys[7],"G")
  vrlc.setNote(keys[8],"G#")
  vrlc.setNote(keys[9],"A")
  vrlc.setNote(keys[10],"A#")
  vrlc.setNote(keys[11],"B")
setNotes()

def background():
  ground = vrlc.entity({
   "class": "collidable",
   "geometry": "primitive: plane; width: 20; height: 40;",
   "material": "color: gray",
   "position": "0 0 "+str(-AWAY),
   "rotation": "-90 0 0"})
  #left wall
  wall1=wall("-10 1 -26", "0.1 2 8")
  #right wall
  wall2=wall("10 1 -26", "0.1 2 8")
  #back wall
  wall3=wall("0 1 -30", "20 2 0.1")
background()

#testing out objects
sphere=sphere=vrlc.entity({
      "class": "collidable",
   	  "geometry": "primitive: sphere",
      "material": "color: red",
      "position": "9 1 0",
      "rotation": "90 90 90"})
def shapes():
	vrlc.entity({
      "class": "collidable",
   	  "geometry": "primitive: dodecahedron",
      "material": "color: blue",
      "position": "-9 1 0",
      "rotation": "90 90 90"})
	sphere=vrlc.entity({
      "class": "collidable",
   	  "geometry": "primitive: sphere",
      "material": "color: red",
      "position": "9 1 0",
      "rotation": "90 90 90"})
#shapes()

#vrlc.setAttrib(sphere, "color", "green")
#vrlc.setColor(sphere, "green")
'''
# Set up an event handler for the right hand Oculus controller A button:
def handleRightA(event):
  sphere2=vrlc.entity({
      "class": "collidable",
      "geometry": "primitive: sphere",
      "material": "color: blue",
      "position": "9 1 5",
      "rotation": "90 0 0"})
  #vrlc.setAttrib(sphere2, "position", "9 5 5")
  #vrlc.setScale(sphere2, 0.5, 1, 1)

# Create the Javascript proxy for the handler and add it as an event listener.
handleRightAProxy = makeHandler('abuttondown', 'right-hand', handleRightA)


import random
# Set up an event handler for the right hand Oculus controller B button:
# Pressing it will cause a cube to appear.
def handleRightB(event):
  print("handleRightB was called with this event:", event)
  box2 = vrlc.box()
  vrlc.setColor(box2, random.choice(["green", "red", "magenta", "black", "gray"]))
  vrlc.setPosition(box2, 6, 0, -7)

# Create the Javascript proxy for the handler and add it as an event listener.
handleRightBProxy = makeHandler('bbuttondown', 'right-hand', handleRightB)

# Set up an event handler for the left hand Oculus controller Y button:
# Pressing it will cause a cube to appear.
def handleLeftY(event):
  print("handleLeftY was called with this event:", event)
  print(event.printMousePos)
  event.position_string
  box2 = vrlc.box()
  vrlc.setColor(box2, random.choice(["green", "red", "magenta", "black", "gray"]))
  vrlc.setPosition(box2, 6, 0, 7)

# Create the Javascript proxy for the handler and add it as an event listener.
handleLeftYProxy = makeHandler('ybuttondown', 'left-hand', handleLeftY)
'''
