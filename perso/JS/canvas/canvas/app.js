const canvas = document.querySelector('canvas');
let ctx = canvas.getContext('2d');

ctx.arc(50, 50, 75, 0, 2*Math.PI, false);
ctx.stroke();