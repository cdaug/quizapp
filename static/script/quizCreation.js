function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

var QUIZCREATION = (function() {

  var Evt = new EventEmitter2();

  var select_el;

  select_el = $('#selectElement')

  function checkType() {
    alert(select_el.options)
  }

  function init() {
    select_el.on('change', checkType())
  };

  return {
    init: init,
  };

})();

ready(QUIZCREATION.init);
