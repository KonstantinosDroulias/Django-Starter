document.addEventListener("DOMContentLoaded", function() {
    // Select all alerts inside the toast container
    const messages = document.querySelectorAll('#toast-container .alert');

    messages.forEach(function(message) {
        // Set a timeout to start the fade out after 3 seconds
        setTimeout(function() {
            message.style.opacity = '0';
            message.style.transform = 'translateY(-20px)';
            message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

            // Remove from DOM after the transition finishes
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 3000);
    });
});