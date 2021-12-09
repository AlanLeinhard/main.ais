
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

$('.responsive').slick({
    dots: true,
    infinite: false,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

 