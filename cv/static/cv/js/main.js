
// Functions for toggling themes
document.getElementsByTagName("link")[1].setAttribute("href", "static/cv/css/main.css");

function changeThemeToDark() {
  document.getElementsByTagName("link")[2].setAttribute("href", "static/cv/css/dark.css");
}

function changeThemeToLight() {
  document.getElementsByTagName("link")[2].setAttribute("href", "");
}



function getWidth() {
  if (self.innerWidth) {
    return self.innerWidth;
  }

  if (document.documentElement && document.documentElement.clientWidth) {
    return document.documentElement.clientWidth;
  }

  if (document.body) {
    return document.body.clientWidth;
  }
}

function myFunction() {
  var x = getWidth()
  if (x<=768){
    var element = document.getElementById("nav_toggle");
    element.classList.toggle("show");
    var x = getWidth()
  }
  if (x>768) {
    var element = document.getElementById("nav_toggle");
  }
}

