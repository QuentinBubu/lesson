let canvas = document.querySelector("canvas")
let ctx = canvas.getContext('2d')

ctx.beginPath();
ctx.arc(75, 75, 50, 0, 2 * Math.PI);
ctx.stroke();

function changeHour() {
}