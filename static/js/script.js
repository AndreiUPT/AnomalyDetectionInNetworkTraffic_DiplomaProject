// script.js
/*$(document).ready(function() {
    // Handle form submission
    $("#prediction-form").submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        var formData = {
            source: $("#source").val(),
            destination: $("#destination").val(),
            protocol: $("#protocol").val(),
            length: $("#length").val()
        };

        // Send form data to server for prediction
        $.ajax({
            url: "/predict",
            method: "POST",
            data: formData,
            success: function(response) {
                console.log("Prediction response:", response); // Log prediction response
                // Update UI with prediction result
                $("#prediction-result").text("Prediction: " + response.prediction);
            },
            error: function(xhr, status, error) {
                // Handle error
                console.error(xhr.responseText);
            }
        });
    });
});
*/