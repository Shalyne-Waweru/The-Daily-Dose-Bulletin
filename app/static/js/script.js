// Add active class to the current nav button
let header = document.getElementById("navBtns");
let btns = header.getElementsByClassName("btn");
for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    let current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

// const ul = document.querySelectorAll('ul li');
//     for (let i = 0; i <= ul.length - 1; i++) {
//         alert(ul[i]);
//     }