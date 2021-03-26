
// alert("Hi!")

document.addEventListener("DOMContentLoaded", changeColor);

function changeColor() {
    var element = document.querySelector("div");
    element.style.color = "green";
}

const btn = document.querySelector("button");

btn.addEventListener("click", redColor);

function redColor() {
    const txt = document.querySelector("div");
    txt.style.color = "red"
}