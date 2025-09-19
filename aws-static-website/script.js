function greetUser() {
    const name = document.getElementById('nameInput').value;
    const greeting = document.getElementById('greeting');

    if(name.trim() === "") {
        greeting.textContent = "Please enter your name!";
        greeting.style.color = "red";
    } else {
        greeting.textContent = `Hello, ${name}! Welcome to my AWS Portfolio!`;
        greeting.style.color = "green";
    }
}
