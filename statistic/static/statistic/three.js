// jquery.min.js
// bootstrap.min.js
// propeller.js
// circles.min.js

$(document).ready(function() {
    var sPath=window.location.pathname;
    var sPage = sPath.substring(sPath.lastIndexOf('/') + 1);
    $(".pmd-sidebar-nav").each(function(){
        $(this).find("a[href='"+sPage+"']").parents(".dropdown").addClass("open");
        $(this).find("a[href='"+sPage+"']").parents(".dropdown").find('.dropdown-menu').css("display", "block");
        $(this).find("a[href='"+sPage+"']").parents(".dropdown").find('a.dropdown-toggle').addClass("active");
        $(this).find("a[href='"+sPage+"']").addClass("active");
    });
});

(function() {
"use strict";
var toggles = document.querySelectorAll(".c-hamburger");
for (var i = toggles.length - 1; i >= 0; i--) {
var toggle = toggles[i];
toggleHandler(toggle);
};
function toggleHandler(toggle) {
toggle.addEventListener( "click", function(e) {
  e.preventDefault();
  (this.classList.contains("is-active") === true) ? this.classList.remove("is-active") : this.classList.add("is-active");
});
}

})();

function progress(percent, $element) {
    var progressBarWidth = percent * $element.width() / 100;
    $element.find('.progress-bar').animate({ width: progressBarWidth }, 500);
} 

progress(50, $('.cash-progressbar'));
progress(30, $('.card-progressbar'));
progress(60, $('.wallet-progressbar'));
progress(40, $('.credit-progressbar'));
progress(10, $('.other-progressbar'));

    var colors = [
        ['#dfe3e7', '#f79332'], ['#dfe3e7', '#f79332'], ['#dfe3e7', '#f79332'], ['#dfe3e7', '#2ab7ee'], ['#dfe3e7', '#00719d']
    ], circles = [];
    for (var i = 1; i <= 3; i++) {
        var child = document.getElementById('circles-' + i),
            percentage = 10 + (i * 8);

        circles.push(Circles.create({
            id:         child.id,
            value:		percentage,
            radius:     50,
            width:      7,
            colors:     colors[i - 1],
             textClass:           'circles-text',
              styleText:           true
        }));
    }


