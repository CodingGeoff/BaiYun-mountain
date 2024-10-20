$(document).ready(function() {
    $('#testimonialForm').submit(function(e) {
        e.preventDefault();

        var name = $('#name').val();
        var email = $('#email').val();
        var testimonial = $('#testimonial').val();

        // Send data to the server for processing
        $.ajax({
            url: '/submit_testimonial', // Replace with your Flask route
            type: 'POST',
            data: {
                name: name,
                email: email,
                testimonial: testimonial
            },
            success: function(response) {
                // Handle successful submission (e.g., display a thank you message)
                alert('Testimonial submitted successfully!');
                $('#name').val('');
                $('#email').val('');
                $('#testimonial').val('');
            },
            error: function(error) {
                // Handle errors (e.g., display an error message)
                console.error('Error submitting testimonial:', error);
            }
        });
    });
});