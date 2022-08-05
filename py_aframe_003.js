// Here is a library of Python-callable Javascript functions for creating and
// modifying AFrame (and also Three.js) representations of VR geometry.
//
//
// Last updated: Feb. 2, 2022.     S. Tanimoto, Jan. 14, 2022.

// First, some code to support teleporting.  I guess this could go in the
// main file instead, but why not here.

    AFRAME.registerComponent("input-listen", {
        init: function () {
            //X-button Pressed
            this.el.addEventListener("xbuttondown", function (e) {
                  this.emit("teleportstart");
            });

            //X-button Released
            this.el.addEventListener("xbuttonup", function (e) {
                this.emit("teleportend");
            });
        }
    });
var vrdiv = document.getElementById("vrstuff");


// Get our default AFrame scene definition HTML for use in setting and
// re-setting the VR content of the user's app.
var standard_starting_a_frame_scene;
retrieve_file("starter-a-scenes/multiplayer.afr").then(function(txt) {
  standard_starting_a_frame_scene = txt; });
function jsPlayNote(note)
  {
  	context = new AudioContext;
  	oscillator = context.createOscillator();
  	if (note=="C") {
      	oscillator.frequency.value = 261.63;
      }
      if (note=="C#") {
      	oscillator.frequency.value = 277.18;
      }
      if (note=="D") {
      	oscillator.frequency.value = 293.66;
      }
      if (note=="D#") {
      	oscillator.frequency.value = 311.13;
      }
      if (note=="E") {
      	oscillator.frequency.value = 329.63;
      }
      if (note=="F") {
      	oscillator.frequency.value = 349.23;
      }
      if (note=="F#") {
      	oscillator.frequency.value = 369.99;
      }
      if (note=="G") {
      	oscillator.frequency.value = 392;
      }
      if (note=="G#") {
      	oscillator.frequency.value = 415.30;
      }
      if (note=="A") {
      	oscillator.frequency.value = 440;
      }
      if (note=="A#") {
      	oscillator.frequency.value = 466.16;
      }
      if (note=="B") {
      	oscillator.frequency.value = 493.88;
      }
  	oscillator.connect(context.destination);
  	oscillator.start(0);
      stopNote(oscillator)
  }
function stopNote(oscillator)
  {
  	setTimeout(function(){
      	oscillator.stop(0);
  	}, 2000);
  }

//function jsPrintMousePos(event) {
  //  console.log("clientX: " + event.clientX + " - clientY: " + event.clientY);
  //}

  //document.addEventListener("click", printMousePos);
  
var py_aframe = {


 // This is a function to remove the AFrame content from the DOM.
 // It's somewhat redundant with the "Run (and reset VR)" functionality, but
 // could be useful in a future Python REPL that we might add to the app.
 // It does initialize an empty scene (with teleport controls),
 // which the Run button does not do.
 clear: function () {
  vrdiv = document.getElementById("vrstuff");
  vrdiv.innerHTML = standard_starting_a_frame_scene;
 },

 // This function makes the standard AFrame starting demo invokable from Python.
 hello_aframe: function () {
  alert("Testing the VR stuff.");

  vrdiv = document.getElementById("vrstuff");
  vrdiv.innerHTML =
    '  <a-scene id="the_scene" embedded vr-mode-ui>'
    +'   <a-entity id="left-hand" oculus-touch-controls="hand: left" teleport-controls></a-entity>'
    +'   <a-entity id="right-hand" oculus-touch-controls="hand: right" teleport-controls></a-entity>'
    +'   <a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>'
    +'   <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>'
    +'   <a-cylinder position="1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>'
    +'   <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>'
    +'   <a-sky color="#ECECEC"></a-sky>'


    +'   <a-entity id="cameraRig">'
    +'     <a-entity id="head" camera wasd-controls look-controls position="0 1.6 0"></a-entity>'
    +'     <a-entity id="ctlL"'
    +'       teleport-controls="cameraRig: #cameraRig;'
    +'       teleportOrigin: #head; startEvents: teleportstart; endEvents: teleportend"'
    +'       raycaster="objects: .collidable; far:1.2;" laser-controls="hand: left" input-listen>'
    +'       <a-text value="X: Teleport" position="0 0.05 0" rotation="-90 0 0"'
    +'         scale="0.1 0.1 0.1" align="center" color="#FFFFFF"></a-text>'
    +'       </a-entity>'
    +'     <a-entity id="ctlR" raycaster="objects: .collidable; far:1.2;"'
    +'       laser-controls="hand: right" input-listen>'
    +'       <a-text value="This is your hand!"'
    +'            position="0 0.05 0" rotation="-90 0 0" scale="0.1 0.1 0.1"'
    +'            align="center" color="#FFFFFF"></a-text>'
    +'       </a-entity>'
    +'     </a-entity>'
    +'   </a-scene>';
 },

 // Here's a function to create almost any kind of entity that AFrame permits.
 // The argument, in the Python code, should be a dict giving property-value pairs.
 // The format for these pairs corresponds to the AFrame entity documentation examples.
 // Most of the values will be strings, even for multi-value properties such as position.
 entity: function( propertyObjectProxy ) {
  //console.log("Calling vrlc.entity");
  //console.log(propertyObjectProxy);
  propertyObject = propertyObjectProxy.toJs({dict_converter: Object.fromEntries});
  //console.log(propertyObject);
  let scene = document.getElementById("the_scene");
  let node = document.createElement("a-entity");
  for (const [prop, value] of Object.entries(propertyObject)) {
    //console.log("prop="+prop+", value="+value); // Helps debug the AFrame property specifications.
    node.setAttribute(prop, value);
  }
  scene.appendChild(node);
  return node;
 },

 // Here is one specialized entity constructor that makes creating cubes easy.
 box: function (note_type) {
  let scene = document.getElementById("the_scene");
  let node = document.createElement("a-box");
  node.setAttribute("color", "purple");
//  node.setAttribute("note",note_type)
  node.object3D.position.set(-0.5, 0.5, -2); // Position updating is supposed to
    // be handled differently than color, accoding to the AFrame docs.  Here we
    // directly set the Three.js object's property.
  scene.addEventListener("click", function () {
//          jsPlayNote(node.getAttribute(note));
  console.log(event);
//with the click, we get x and y coordinates.
//in the 3d space, if we get x, y, and z, we can find out the click is at the box and play note.
  jsPlayNote("A");
      })

  scene.appendChild(node);
  //jsPlayNote("A")
  return node;
 },
 // General function for updating an entity property.
 setAttrib: function( entity, property, attribute ) {
  // Should work for most properties. (Not recommended for position or rotation, though)
  entity.setAttribute(property, value);
 },
 // Specific function for updating the position of an entity.
 // Note that it directly updates the Three.js representation of the entity,
 // bypassing AFrame (as recommended in the AFrame docs).
 setPosition: function (entity, x, y, z) {
  entity.object3D.position.set(x, y, z);
 },

 onClick: function(entity) {
   jsPlayNote(entity.getAttribute("note"))
},
 // Similar updater for rotation.
 setRotation: function (entity, a1, a2, a3) {
  entity.object3D.rotation.set(a1, a2, a3);
 },
 // Similar updater for scale.
 setScale: function (entity, sx, sy, sz) {
  entity.object3D.scale.set(sx, sy, sz);
 },
 // A convenience function for updating color.
 setColor: function (entity, color) {
  entity.setAttribute("color",color);
 },
 setNote: function(entity,noteString) {
   //alert("Testing the note stuff.");
   entity.setAttribute("note",noteString)
 },
 playNote: function(entity) {
   jsPlayNote(entity.getAttribute("note"))
 }
}
