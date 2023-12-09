document.addEventListener("DOMContentLoaded", function () {
  // Get all favorite buttons
  var favoriteButtons = document.querySelectorAll(".favorite-btn");

  // Add click event listener to each favorite button
  favoriteButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      // Toggle the 'active' class to change the color
      button.classList.toggle("active");

      // Check if the button is unclicked (does not have the "active" class)
      if (!button.classList.contains("active")) {
        // Get the parent food box
        var foodBox = button.closest(".food-box");

        // Retrieve data attributes from the food box
        var recipeuri = foodBox.getAttribute("data-uri");

        // Create an object with the retrieved data
        var foodData = {
          uri: JSON.parse(recipeuri)
        };

        // Send the request to the backend using an AJAX request
        fetch('/remove_selected_food', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(foodData),
        })
        .then(response => response.json())
        .then(data => {
          console.log('Success (Remove):', data);
          // Optionally update the UI or perform additional actions
        })
        .catch((error) => {
          console.error('Error (Remove):', error);
          // Handle errors or display an error message
        });
      }
    });
  });
});
