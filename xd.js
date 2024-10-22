let angulo = 0;
let rotacion;

function verificarPeso() {
    const peso = parseFloat(document.getElementById('peso').value);
    const imagen = document.getElementById('imagen');
    const musica = document.getElementById('musica');

    if (peso > 100) {
        // Mostrar la imagen y reproducir música
        imagen.style.display = 'block';
        musica.play();
        // Iniciar rotación
        rotacion = setInterval(() => {
            angulo += 2;
            imagen.style.transform = `rotate(${angulo}deg)`;
        }, 100);
    } else {
        alert('Tu peso no supera los 100 kg.');
    }
}