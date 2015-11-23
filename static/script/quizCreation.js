function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var QUIZCREATION = (function() {

  var Evt = new EventEmitter2();

  var select_el, creationArea, multipleChoice;

  creationArea = $('#creationArea');
  multipleChoice = $('#multipleChoice');
  saa = $('#selectAllApplying');
  shortAnswer = $('#shortAnswer');
  matching = $('#matching');
  undetermined = $('#undetermined');


  function checkType() {
    quizType = $(this).val();
    console.log(quizType);
    if (quizType === 'multipleChoice') {
      creationArea.text('You have selected a Multiple Choice Quiz.');
      Evt.emit('quizSelected', quizType);
    }
    else if (quizType === 'matching') {
      creationArea.text('You have selected a Matching Quiz.');
      Evt.emit('quizSelected', quizType);
    }
    else if (quizType === 'selectAllApplying') {
      creationArea.text('You have selected a Select All Applying Quiz.');
      Evt.emit('quizSelected', quizType);
    }
    else if (quizType === 'shortAnswer') {
      creationArea.text('You have selected a Short Answer Quiz.');
      Evt.emit('quizSelected', quizType);
    }
    else {
      creationArea.text('Please select a quiz type to start creating it here.');
    }
  }

  function createQuiz(e) {
    
  }

  function init() {
    multipleChoice.on('click', checkType);
    saa.on('click', checkType);
    shortAnswer.on('click', checkType);
    matching.on('click', checkType);
    undetermined.on('click', checkType);
    Evt.addListener('quizSelected', createQuiz);
    creationArea.text('Please select a quiz type to start creating it here.');
  }

  return {
    init: init,
  };

})();

ready(QUIZCREATION.init);
