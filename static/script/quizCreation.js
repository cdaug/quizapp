function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var QUIZCREATION = (function() {

  var Evt = new EventEmitter2();

  var autoGradeButton, manualGradeButton;
  autoGradeButton = $('#autoGradeButton');
  manualGradeButton = $('#manuallyGradeButton');
  hiddenInput = $('#hiddenthing');

  function setupAuto() {
    alert('Starting Automatically Graded Quiz');
    $(this).velocity({'opacity': '-25'}, {duration: "slow"});
    manualGradeButton.velocity({'opacity': '-25'}, {duration: "slow"});
    manualGradeButton.remove();
    autoGradeButton.remove();
    hiddenInput.velocity({'opacity': '25'}, {duration: "5000"});
  }

  function setupManual() {
    alert('Starting Manually Graded Quiz');
    $(this).velocity({'opacity': '-25'}, {duration: "5000"});
    autoGradeButton.velocity({'opacity': '-25'}, {duration: "5000"});
    autoGradeButton.remove();
    manualGradeButton.remove();
    hiddenInput.velocity({'opacity': '25'}, {duration: "5000"});
  }

  function init() {
    hiddenInput.velocity({'opacity': '-25'}, {duration: "fast"});
    autoGradeButton.on('click', setupAuto);
    manualGradeButton.on('click', setupManual);
  }

  return {
    init: init,
  };

})();

ready(QUIZCREATION.init);
