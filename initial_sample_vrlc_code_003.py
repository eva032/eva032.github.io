import py_aframe as vrlc
vrlc.clear() # Create empty a-scene.

import random

vrlc.a_entity("a-entity", "the_scene","mouseCursor","cursor~rayOrigin:mouse,raycaster~objects:.intersectable")
vrlc.a_entity("a-entity", "the_scene","e1","position~0 .6 4")
vrlc.a_entity("a-camera", "e1","c1", "")
vrlc.a_entity("a-entity", "c1","e4","raycaster~far:30;objects:.intersectable,cursor~,geometry~primitive:ring;radiusOuter:0.015;radiusInner:0.01;segmentsTheta:32,material~color:#283644;shader:flat,position~0 0 -0.75")

#vrlc.CreateEntity(mixInObj, OuterObj, InnerObj, jsEvt_Click, jsEvt_MouseEnter)
vrlc.CreateEntity("geometry~primitive:box,material~color:#F35F5F",
					"position~3.5 1 0",
					"class~intersectable,animation~startEvents:click; property: position; from: 0 0 0; to: 0 0 -10; dur: 2000",
					"jsPlayNote('E')",
					"jsPlayNote('A')")

vrlc.CreateEntity("geometry~primitive:cylinder,material~color:crimson,height:3,radius~1.5",
					"position~1.8 2.1 1",
					"class~intersectable,animation~startEvents:click; property: position; from: 0 0 0; to: 0 0 -10; dur: 2000",
					"jsPlayNote('E')",
					"jsPlayNote('A')")

vrlc.CreateEntity("geometry~primitive:ring,material~color:blue,radius-inner:3,radius-outer~1.5",
					"position~0.8 1.1 2",
					"class~intersectable,animation~startEvents:click; property: position; from: 0 0 0; to: 0 0 -10; dur: 2000",
					"jsPlayNote('E')",
					"jsPlayNote('A')")