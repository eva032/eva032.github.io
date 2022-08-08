import py_aframe as vrlc
vrlc.clear() # Create empty a-scene.

import random

vrlc.a_entity("audio", "a_assets","blip1","crossorigin~anonymous,preload~auto,src~https://assets.mixkit.co/sfx/download/mixkit-arcade-game-jump-coin-216.wav")
vrlc.a_entity("audio", "a_assets","blip2","crossorigin~anonymous,preload~auto,src~https://assets.mixkit.co/sfx/download/mixkit-positive-interface-beep-221.wav")
vrlc.a_entity("audio", "a_assets","shot","crossorigin~anonymous,preload~auto,src~https://assets.mixkit.co/sfx/download/mixkit-quick-win-video-game-notification-269.wav")
vrlc.a_entity("a-mixin", "a_assets","cube","geometry~primitive:box")
vrlc.a_entity("a-mixin", "a_assets","red","material~color:#F35F5F")

vrlc.a_entity("a-entity", "the_scene","mouseCursor","cursor~rayOrigin:mouse,raycaster~objects:.intersectable")
vrlc.a_entity("a-entity", "the_scene","e1","position~0 .6 4")

vrlc.a_entity("a-camera", "e1","c1", "")
vrlc.a_entity("a-entity", "c1","e4","raycaster~far:30;objects:.intersectable,cursor~,geometry~primitive:ring;radiusOuter:0.015;radiusInner:0.01;segmentsTheta:32,material~color:#283644;shader:flat,position~0 0 -0.75")

vrlc.a_entity("a-entity", "the_scene","e5","position~-3.5 1 0")
vrlc.a_entity("a-entity", "e5","e7","mixin~red cube,class~intersectable,sound__1~on: click; src: #shot,sound__2~on: mouseenter; src: #blip2,animation~startEvents:click; property: position; from: 0 0 0; to: 0 0 -10; dur: 2000")

vrlc.a_entity("a-entity", "the_scene","e6","position~3.5 1 0,rotation~0 45 0")
vrlc.a_entity("a-entity", "e6","e8","mixin~blue cube,class~intersectable,sound__1~on: click; src: #shot,sound__2~on: mouseenter; src: #blip2,animation~startEvents: click; loop: 1; dir: alternate; property: position; from: 0 0 0; to: 15 0 0; dur: 2000")
