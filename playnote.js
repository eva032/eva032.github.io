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
    }, 1000);
  }
