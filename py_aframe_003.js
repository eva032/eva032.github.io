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
function jsPlayNote(note) {
    context = new AudioContext;
    oscillator = context.createOscillator();
    if (note == "C") {
        oscillator.frequency.value = 261.63;
    }
    if (note == "C#") {
        oscillator.frequency.value = 277.18;
    }
    if (note == "D") {
        oscillator.frequency.value = 293.66;
    }
    if (note == "D#") {
        oscillator.frequency.value = 311.13;
    }
    if (note == "E") {
        oscillator.frequency.value = 329.63;
    }
    if (note == "F") {
        oscillator.frequency.value = 349.23;
    }
    if (note == "F#") {
        oscillator.frequency.value = 369.99;
    }
    if (note == "G") {
        oscillator.frequency.value = 392;
    }
    if (note == "G#") {
        oscillator.frequency.value = 415.30;
    }
    if (note == "A") {
        oscillator.frequency.value = 440;
    }
    if (note == "A#") {
        oscillator.frequency.value = 466.16;
    }
    if (note == "B") {
        oscillator.frequency.value = 493.88;
    }
    oscillator.connect(context.destination);
    oscillator.start(0);
    stopNote(oscillator)
}
function stopNote(oscillator) {
    setTimeout(function () {
        oscillator.stop(0);
    }, 750);
}

var vrdiv = document.getElementById("vrstuff");



var standard_starting_a_frame_scene;
retrieve_file("starter-a-scenes/multiplayer.afr").then(function (txt) {
    standard_starting_a_frame_scene = txt;
});

var py_aframe = {
    clear: function () {
        vrdiv = document.getElementById("vrstuff");
        vrdiv.innerHTML = standard_starting_a_frame_scene;
    },

    // Here is one specialized entity constructor that makes creating cubes easy.
    a_entity: function (TagName, ParentTagId, id, AttrObj, Evt_Click, Evt_MouseEnter) {
        let BaseTag = document.getElementById(ParentTagId);
        let node = document.createElement(TagName);
        node.setAttribute('id', id);
        BaseTag.appendChild(node);
        node = document.getElementById(id);
        if (AttrObj != null || AttrObj != undefined) {
            let arrVal = AttrObj.split(',');
            for (let iIndex = 0; iIndex < arrVal.length; iIndex++) {
                let arrAttr = arrVal[iIndex].split('~');
                if (arrAttr == null || arrAttr == undefined || arrAttr.length < 2)
                    continue;
                node.setAttribute(arrAttr[0], String(arrAttr[1]));
            }
        }
        Evt_Click = String(Evt_Click);
        Evt_MouseEnter = String(Evt_MouseEnter);

        if (Evt_Click != '') {
            node.addEventListener("click", function () {
                eval(Evt_Click);
            });
        }
        if (Evt_MouseEnter != '') {
            node.addEventListener("mouseenter", function () {
                eval(Evt_MouseEnter);
            });
        }

        return node;
    },
    CreateEntity: function (mixInObj, OuterObj, InnerObj, jsEvt_Click, jsEvt_MouseEnter) {
        let BaseID = String(parseInt(Math.random() * 1000000000)), MixInID = '', OuterEntiryID = '';
        if (mixInObj != null) {
            MixInID = 'm_' + BaseID;
            this.a_entity("a-mixin", "a_assets", MixInID, mixInObj);
        }
        OuterEntiryID = 'eo_' + BaseID;
        this.a_entity("a-entity", "the_scene", OuterEntiryID, OuterObj);
        this.a_entity("a-entity", OuterEntiryID, 'ei_' + BaseID, "mixin~" + MixInID + "," + InnerObj, jsEvt_Click, jsEvt_MouseEnter);
    }
}
