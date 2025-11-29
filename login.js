document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate a login check (you can replace this with real authentication logic)
    if (username === "admin" && password === "password123") {
        alert("Login successful!");
        window.location.href = "card.html"; // Redirect to the new page
    } else {
        alert("Invalid username or password. Try again.");
    }
});
