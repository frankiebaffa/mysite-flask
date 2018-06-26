var modalabout= document.getElementById('modalabout');
var btnabout = document.querySelector('[title="About"]');
var navcollapse = document.querySelector('[class="navbar-toggle collapsed"]');
btnabout.onclick = function() {
    modalabout.style.display = "block";
    navcollapse.click();
}
modalabout.onclick = function() {
    modalabout.style.display = "none";
}
var aboutnav = document.querySelector('[title="About"]');
aboutnav.removeAttribute("href");
