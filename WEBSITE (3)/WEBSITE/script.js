document.addEventListener('mousemove', (e) => {
    document.body.style.backgroundPositionX = e.clientX / -10 + 'px';
    document.body.style.backgroundPositionY = e.clientY / -10 + 'px';
});

// Simulated User Stats
document.getElementById("username").innerText = "CyberHero_42";
document.getElementById("files-count").innerText = Math.floor(Math.random() * 50) + 1;

function logout() {
    alert("Logging out...");
    window.location.href = "index.html";
}
