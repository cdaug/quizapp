function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

function visible() {
  document.getElementById('hiddenbook').style.display="block";
}

function hide() {
  document.getElementById('hiddenbook').style.display="none";
}

function hideAnything(btn) {
  btn.style.display = 'none';
}

ready(hide());
