document.addEventListener('DOMContentLoaded', function() {
    // Other JavaScript code can go here

    // Formspree website for the contact form
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); 
        const form = event.target;
        const formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData,
            headers: {
                Accept: "application/json",
            },
        })
        .then((response) => {
            if (response.ok) {
                document.getElementById("thankYouMessage").style.display = "block";
                form.reset();
                setTimeout(() => {
                    document.getElementById("thankYouMessage").style.display = "none";
                }, 3000);
            } else {
                console.error("Form submission failed");
                // Optionally add more specific error handling here
            }
        })
        .catch((error) => {
            console.error("There was a problem with the fetch operation:", error.message);
            // Optionally add more specific error handling here
        });
    });
});
