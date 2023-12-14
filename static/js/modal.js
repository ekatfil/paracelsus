document.addEventListener("DOMContentLoaded", function () {
    const noteModal = document.getElementById("noteModal");
    const closeModalBtn = document.querySelector(".close-notes-modal");
    const createnoteModal = document.getElementById("createnoteModal");
    const addNoteBtn = document.getElementById("add-note");
    const saveNoteBtn = document.getElementById("save-note");
    const calendarTable = document.getElementById("calendarTable");
    const closeCreateNoteModalBtn = createnoteModal.querySelector(".close-create-modal");

    calendarTable.addEventListener("click", function (event) {
        const clickedElement = event.target;
        if (clickedElement.tagName === "TD") {
            noteModal.classList.add("visible");
        }
    });

    closeModalBtn.addEventListener("click", function () {
        noteModal.classList.remove("visible");
    });

    addNoteBtn.addEventListener("click", function () {
        noteModal.classList.remove("visible");
        createnoteModal.classList.add("visible");
    });

    saveNoteBtn.addEventListener("click", function () {
        createnoteModal.classList.remove("visible");
        noteModal.classList.add("visible");
    });

    closeCreateNoteModalBtn.addEventListener("click", function () {
        createnoteModal.classList.remove("visible");
        noteModal.classList.add("visible");
    });

    window.addEventListener("click", function (event) {
        if (event.target === noteModal) {
            noteModal.classList.remove("visible");
        }
        if (event.target === createnoteModal) {
            createnoteModal.classList.remove("visible");
            noteModal.classList.add("visible"); 
        }
    });
});

