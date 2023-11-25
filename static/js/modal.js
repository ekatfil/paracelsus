document.addEventListener("DOMContentLoaded", function () {
    // ... your existing code ...

    // Get modal elements
    const noteModal = document.getElementById("noteModal");
    const closeModalBtn = document.querySelector(".close");

    // Open the modal when a day is clicked
    calendarTable.addEventListener("click", function (event) {
        const clickedElement = event.target;
        if (clickedElement.tagName === "TD") {
            // You may want to implement logic to identify the specific day clicked
            // For simplicity, let's assume you have a function getDayFromDate() that returns the day

            // Open the modal here
            noteModal.style.display = "block";
        }
    });

    // Close the modal when the close button is clicked
    closeModalBtn.addEventListener("click", function () {
        noteModal.style.display = "none";
    });

    // Close the modal if the user clicks outside of it
    window.addEventListener("click", function (event) {
        if (event.target === noteModal) {
            noteModal.style.display = "none";
        }
    });
});
