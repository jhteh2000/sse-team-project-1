// ... Other parts of your JavaScript code

document.addEventListener("DOMContentLoaded", function () {
  // Get all favorite buttons
  var favoriteButtons = document.querySelectorAll(".favorite-btn");

  // Add click event listener to each favorite button
  favoriteButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      // Toggle the 'active' class to change the color
      button.classList.toggle("active");

      // Get the parent food box
      var foodBox = button.closest(".food-box");

      // Retrieve data attributes from the food box
      var ingredientList = foodBox.getAttribute("data-ingredientlist");
      var recipeURL = foodBox.getAttribute("data-recipeurl");
      var name = foodBox.querySelector("h3").innerText;
      var image = foodBox.querySelector("img").src;
      var calories = foodBox.querySelector(".details p:nth-child(1)").innerText.split(":")[1].trim();
      var protein = foodBox.querySelector(".details p:nth-child(2)").innerText.split(":")[1].trim();

      // Create an object with the retrieved data
      var foodData = {
        ingredientList: JSON.parse(ingredientList),
        recipeURL: JSON.parse(recipeURL),
        name: name,
        image: image,
        calories: calories,
        protein: protein
      };

      // Log the data or send it to the backend
      console.log(foodData);

      // Send the data to the backend using an AJAX request
      fetch('/add_selected_food', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(foodData),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        // Optionally update the UI or perform additional actions
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle errors or display an error message
      });
    });
  });
});

