import py_aframe as vrlc
vrlc.clear() # Create empty a-scene.

#setting up the scene
vrlc.a_entity("a-entity", "the_scene","mouseCursor","cursor~rayOrigin:mouse,raycaster~objects:.intersectable")
vrlc.a_entity("a-entity", "the_scene","e1","position~0 .6 4")
vrlc.a_entity("a-camera", "e1","c1", "")
vrlc.a_entity("a-entity", "c1","e4","raycaster~far:30;objects:.intersectable,cursor~,geometry~primitive:ring;radiusOuter:0.015;radiusInner:0.01;segmentsTheta:32,material~color:#283644;shader:flat,position~0 0 -0.75")

#vrlc.CreateEntity(mixInObj, OuterObj, InnerObj, jsEvt_Click, jsEvt_MouseEnter)
#creating 12 boxes to represent 12 keys
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~-7.5 0 -5",
					"class~intersectable",
					"jsPlayNote('C')",
					"jsPlayNote('C')")
vrlc.CreateEntity("geometry~primitive:box,material~color:blue",
					"position~-6 0 -6",
					"class~intersectable",
					"jsPlayNote('C#')",
					"jsPlayNote('C#')")

vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~-4.5 0 -5",
					"class~intersectable",
					"jsPlayNote('D')",
					"jsPlayNote('D')")
vrlc.CreateEntity("geometry~primitive:box,material~color:blue",
					"position~-3 0 -6",
					"class~intersectable",
					"jsPlayNote('D#')",
					"jsPlayNote('D#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~-1.5 0 -5",
					"class~intersectable",
					"jsPlayNote('E')",
					"jsPlayNote('E')")
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~0 0 -5",
					"class~intersectable",
					"jsPlayNote('F')",
					"jsPlayNote('F')")
vrlc.CreateEntity("geometry~primitive:box,material~color:blue",
					"position~1.5 0 -6",
					"class~intersectable",
					"jsPlayNote('F#')",
					"jsPlayNote('F#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~3 0 -5",
					"class~intersectable",
					"jsPlayNote('G')",
					"jsPlayNote('G')")
vrlc.CreateEntity("geometry~primitive:box,material~color:blue",
					"position~4.5 0 -6",
					"class~intersectable",
					"jsPlayNote('G#')",
					"jsPlayNote('G#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~6 0 -5",
					"class~intersectable",
					"jsPlayNote('A')",
					"jsPlayNote('A')")
vrlc.CreateEntity("geometry~primitive:box,material~color:blue",
					"position~7.5 0 -6",
					"class~intersectable",
					"jsPlayNote('A#')",
					"jsPlayNote('A#')")
vrlc.CreateEntity("geometry~primitive:box,material~color:white",
					"position~9 0 -5",
					"class~intersectable",
					"jsPlayNote('B')",
					"jsPlayNote('B')")
