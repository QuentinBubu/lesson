var position = 0; //definition a 0

function hideShow() { // fonction
    var css = document.getElementById("boutton4"); // on attribut a l'element css la  l'id
    if (!position) { // Si position est different de 1
        position++; // on incremente
        css.style.backgroundColor = "white"; //j'ai mis background color mais tu personnalise :)
    } else { // et sionon
        position--; // on decremente
        css.style.backgroundColor = "chartreuse";
    }
}