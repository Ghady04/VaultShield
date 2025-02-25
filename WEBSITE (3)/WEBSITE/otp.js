// Countdown Timer
let timeLeft = 60;
let countdown = setInterval(function () {
    document.getElementById("countdown").innerText = timeLeft;
    timeLeft--;

    if (timeLeft < 0) {
        clearInterval(countdown);
        document.getElementById("otp-timer").innerText = "OTP expired!";
        document.getElementById("resend-btn").classList.remove("hidden"); // Show Resend Button
    }
}, 1000);

// Verify OTP Function
function verifyOTP() {
    let enteredOTP = document.getElementById("otp-input").value;

    if (enteredOTP.length > 0) { // Accept any input as OTP
        let fileName = localStorage.getItem("fileToRetrieve");

        // ✅ Show success popup
        document.getElementById("otp-success-popup").style.display = "flex";

        // Simulate file download after delay
        setTimeout(() => {
            window.location.href = "download.html?file=" + encodeURIComponent(fileName);
        }, 3000); // 3-second delay before redirection
    } else {
        alert("⚠️ Please enter an OTP.");
    }
}

// Function to Resend OTP
function resendOTP() {
    alert("🔄 New OTP sent to your email!");
    location.reload(); // Reload page to restart timer
}

// Function to Return to Home
function returnToHome() {
    window.location.href = "dashboard.html";
}
