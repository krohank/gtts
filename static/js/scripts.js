// Validate input text before form submission
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("tts-form");
    const textarea = document.getElementById("text-input");

    form.addEventListener("submit", (event) => {
        if (textarea.value.trim() === "") {
            alert("Please enter some text to convert!");
            event.preventDefault(); // Prevent form submission
        }
    });
});
