

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


        function OnSelectionChange (select) {
            alert(select);
            document.getElementById(main).innerHTML = document.getElementById(p_yandex).innerHTML;
        }

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
