document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('welcome-container');

    // Add animation class after a short delay
    setTimeout(function() {
        container.classList.add('show');
    }, 500); // Adjust the delay based on your preference
});
