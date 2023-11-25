// Function to toggle dropdown visibility
function toggleDropdown(dropdown) {
    dropdown.classList.toggle("hidden");
  }
  
  // Window load event to ensure all elements are present
  window.onload = function () {
    // Get the dropdown buttons
    const navbarUserButton = document.querySelector("[data-collapse-toggle='navbar-user']");
  
    // Get the dropdown menus
    const navbarUser = document.getElementById("navbar-user");
  
    // Event listeners for dropdown buttons
    navbarUserButton.addEventListener("click", () => toggleDropdown(navbarUser));
  };
  