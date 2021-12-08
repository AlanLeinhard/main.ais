
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

  function openCity(evt, cityName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
 document.getElementById(main).innerHTML = document.getElementById(p_yandex).innerHTML;



function openServ(evt, title) {
 var i, tabcontente, tablinkse;

 tabcontente = document.getElementsByClassName("tabcontente");
for (i = 0; i < tabcontente.length; i++) {
tabcontente[i].style.display = "none";
 }
    
 tablinkse = document.getElementsByClassName("tablinkse");
for (i = 0; i < tablinkse.length; i++) {
tablinkse[i].className = tablinkse[i].className.replace(" active", "");
 }
 document.getElementById(title).style.display = "block";
 evt.currentTarget.className += " active";
}


function alerte() {
    alert('Сервис '+(servis_title.value)+' успешно добавлен на главную страницу');
}


function selectcolor() {
    var x = rezultatColor.value;
    fon.style.background = x;
}

var div = document.querySelector('#wrapper div');
document.querySelector('bottom').addEventListener('click', function() {
  var curPos = parseInt(getComputedStyle(div)['left'], 10);
  animate(div, 'left', 'px', curPos, curPos - 100, 500);
  console.log('Y');
}, false);

function animate(elem, style, unit, from, to, time) {
  if (!elem) return;
  var start = new Date().getTime(),
    timer = setInterval(function() {
      var step = Math.min(1, (new Date().getTime() - start) / time);
      elem.style[style] = (from + step * (to - from)) + unit;
      if (step == 1) clearInterval(timer);
    }, 25);
  elem.style[style] = from + unit;
};


$(document).ready(function () {
    $("#makeMeScrollable").smoothDivScroll({
        mousewheelScrolling: "allDirections",
        manualContinuousScrolling: true,
        autoScrollingMode: "onStart"
    });
});

(function () {

    var scrollHandle = 0,
        scrollStep = 5,
        parent = $("#container");

    //Start the scrolling process
    $(".panner").on("mouseenter", function () {
        var data = $(this).data('scrollModifier'),
            direction = parseInt(data, 10);

        $(this).addClass('active');

        startScrolling(direction, scrollStep);
    });

    //Kill the scrolling
    $(".panner").on("mouseleave", function () {
        stopScrolling();
        $(this).removeClass('active');
    });

    //Actual handling of the scrolling
    function startScrolling(modifier, step) {
        if (scrollHandle === 0) {
            scrollHandle = setInterval(function () {
                var newOffset = parent.scrollLeft() + (scrollStep * modifier);

                parent.scrollLeft(newOffset);
            }, 10);
        }
    }

    function stopScrolling() {
        clearInterval(scrollHandle);
        scrollHandle = 0;
    }

}());