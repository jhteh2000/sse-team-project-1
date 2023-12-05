document.addEventListener('DOMContentLoaded', function () {
  const foodBoxes = document.querySelectorAll('.food-box');
  const hoverWindow = document.getElementById('hoverWindow');
  const contentContainer = document.getElementById('contentContainer');
  const closeWindowBtn = document.getElementById('closeWindowBtn');

  foodBoxes.forEach(function (foodBox) {
    foodBox.addEventListener('click', function () {
      // Clear existing content
      contentContainer.innerHTML = '';

      // Add ingredients text
      const ingredients = document.createElement('b');
      ingredients.innerHTML = "Ingredients";
      contentContainer.appendChild(ingredients);

      // Get the content associated with the clicked food box
      const content = foodBox.dataset.ingredientlist;

      try {
        // Try parsing the JSON
        list = JSON.parse(content);

        // Add new content
        for (var i = 0; i < list.length; i++) {
          const paragraph = document.createElement('p');
          paragraph.textContent = list[i];
          contentContainer.appendChild(paragraph);
        }

        hoverWindow.style.display = 'block';
      } catch (error) {
        // Handle parsing error
        console.error('Error parsing JSON:', error);
      }
    });
  });

  closeWindowBtn.addEventListener('click', function () {
    hoverWindow.style.display = 'none';
  });
});
