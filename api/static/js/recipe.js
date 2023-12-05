document.addEventListener('DOMContentLoaded', function () {
  const openWindowLinks = document.querySelectorAll('.openWindowLink');
  const hoverWindow = document.getElementById('hoverWindow');
  const contentContainer = document.getElementById('contentContainer');
  const closeWindowBtn = document.getElementById('closeWindowBtn');

  openWindowLinks.forEach(function(link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();

      // Clear existing content
      contentContainer.innerHTML = '';

      // Get the content associated with the clicked link
      const content = link.dataset.datajson;

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
