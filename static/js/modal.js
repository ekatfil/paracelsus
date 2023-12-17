function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


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
            let date = clickedElement.getAttribute("value");
            console.log(date);
            var pacient_id = '';
            const pacient = document.getElementById('pacient_id');
            if (pacient) {
                pacient_id = pacient.getAttribute("value");
            }

            let data = JSON.stringify({ date: date, pacient_id: pacient_id });

            $.post('/api/get-appointment/', data, function (data) {
                let appointments = data.appointments;
                console.log(appointments);
                const select_date = document.getElementById("date");
                const notes = document.getElementById("notes");
                const data_date = document.getElementById("data-date");
                data_date.setAttribute("data-date", date);
                select_date.innerHTML = "Заметки на " + date + ":";

                while (notes.firstChild) {
                    notes.removeChild(notes.firstChild);
                }

                var div = document.createElement("div");

                var html_text = "";

                appointments.forEach(function (item, i, arr) {
                    var category = "doctor-note";
                    if (item.category == "Личное") {
                        category = "private-note"
                    }


                    if (item.time)
                        html_text += "<div class=\"flex flex-row w-full mb-2 items-center justify-center\"><p class=\"w-1/3\">" + item.time + "</p><div class=\"" + category + " w-2/3 p-2 text-white\">" + item.name + "</div></div>";
                    else
                        html_text += "<div class=\"flex flex-row w-full mb-2 items-center justify-center\"><p class=\"w-1/3\"></p><div class=\"" + category + " w-2/3 p-2 text-white\">" + item.name + "</div></div>"
                });

                div.classList.add("flex", "flex-wrap", "w-full", "items-center", "justify-center");
                div.innerHTML = html_text;
                console.log(div);
                notes.appendChild(div);

            });


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

