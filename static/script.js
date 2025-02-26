document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector("button");
    button.addEventListener("mouseover", function() {
        button.style.backgroundColor = "#9a1f6a";
    });
    button.addEventListener("mouseout", function() {
        button.style.backgroundColor = "#6a0572";
    });
});
