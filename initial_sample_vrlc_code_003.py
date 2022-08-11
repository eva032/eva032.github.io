import py_aframe as vrlc
vrlc.clear() # Create empty a-scene.


vrlc.a_entity("a-entity", "the_scene","mouseCursor","cursor~rayOrigin:mouse,raycaster~objects:.intersectable")
vrlc.a_entity("a-entity", "the_scene","e1","position~0 .6 4")
vrlc.a_entity("a-camera", "e1","c1", "")
vrlc.a_entity("a-entity", "c1","e4","raycaster~far:30;objects:.intersectable,cursor~,geometry~primitive:ring;radiusOuter:0.015;radiusInner:0.01;segmentsTheta:32,material~color:#283644;shader:flat,position~0 0 -0.75")

#vrlc.CreateEntity(mixInObj, OuterObj, InnerObj, jsEvt_Click, jsEvt_MouseEnter)
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~-9 0 -5",
					"class~intersectable",
					"jsPlayNote('C')",
					"jsPlayNote('C')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~-7.5 0 -6",
					"class~intersectable",
					"jsPlayNote('C#')",
					"jsPlayNote('C#')")

vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~-6 0 -5",
					"class~intersectable",
					"jsPlayNote('D')",
					"jsPlayNote('D')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~-4.5 0 -6",
					"class~intersectable",
					"jsPlayNote('D#')",
					"jsPlayNote('D#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~-3 0 -5",
					"class~intersectable",
					"jsPlayNote('E')",
					"jsPlayNote('E')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~0 0 -5",
					"class~intersectable",
					"jsPlayNote('F')",
					"jsPlayNote('F')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~1.5 0 -6",
					"class~intersectable",
					"jsPlayNote('F#')",
					"jsPlayNote('F#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~3 0 -5",
					"class~intersectable",
					"jsPlayNote('G')",
					"jsPlayNote('G')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~4.5 0 -6",
					"class~intersectable",
					"jsPlayNote('G#')",
					"jsPlayNote('G#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~6 0 -5",
					"class~intersectable",
					"jsPlayNote('A')",
					"jsPlayNote('A')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~7.5 0 -6",
					"class~intersectable",
					"jsPlayNote('A#')",
					"jsPlayNote('A#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:pink",
					"position~9 0 -5",
					"class~intersectable",
					"jsPlayNote('B')",
					"jsPlayNote('B')")

def handleRightA(event):
  print("handleRightA was called with this event:", event)
  box2 = vrlc.box()
  vrlc.setColor(box2, random.choice(["green", "red", "magenta", "black", "gray"]))
  vrlc.setPosition(box2, 6, 0, -7)

# Create the Javascript proxy for the handler and add it as an event listener.
handleRightAProxy = makeHandler('abuttondown', 'right-hand', handleRightA)
