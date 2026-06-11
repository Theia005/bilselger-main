document.getElementById("Synkroniserer").onclick = function() {
    fetch("http://127.0.0.1:5000/bil")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById("merke").innerHTML = data[0][1];
        document.getElementById("modell").innerHTML = data[0][2];
        document.getElementById("km").innerHTML = data[0][3];
        document.getElementById("drivstoff").innerHTML = data[0][4];
        document.getElementById("pris").innerHTML = data[0][5];
    });
}