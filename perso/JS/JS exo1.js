var age = parseInt(prompt('Quel est votre âge ? '));
if (age >= 1 && age <= 17) {
    alert('Vous n\'êtes pas majeur');
} else if (age >= 18 && age <= 49) {
    alert('Vous êtes majeur mais pas encore senior!');
} else if (age >= 50 && age <= 59) {
    alert('Vous êtes senior mais pas encore retraité!');
} else if (age >= 60 && age <= 120) {
    alert('Vous êtes à la retraite, profitez bien de votre temps!');
} else if (age < 1) {
    alert('Bah dis donc, vous êtes très jeune!');
} else if (age > 120) {
    alert('Vous avez plus de 120 ans?! Vous m\'épatez!!');
} else {
    alert('Dis donc petit malin, on ne rentre pas son âge? :)');
}