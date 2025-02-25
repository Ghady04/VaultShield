// Function to clear stored files
function clearFiles() {
    localStorage.removeItem("uploadedFiles"); // Remove all stored files
    document.getElementById("file-list").innerHTML = ""; // Clear UI
}

// Attach clearFiles function to a button if needed
document.addEventListener("DOMContentLoaded", function () {
    let clearButton = document.createElement("button");
    clearButton.textContent = "Clear Files";
    clearButton.classList.add("glow-button");
    clearButton.onclick = clearFiles;
    document.querySelector(".retrieve-container").appendChild(clearButton);
});
