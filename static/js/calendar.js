document.addEventListener("DOMContentLoaded", function () {
    const months = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ];

    const calendarTable = document.getElementById("calendarTable");
    const currentMonthYear = document.getElementById("currentMonthYear");
    const prevMonthButton = document.getElementById("prevMonth");
    const nextMonthButton = document.getElementById("nextMonth");

    let currentDate = new Date();

    function renderCalendar() {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        currentMonthYear.textContent  = months[month] + " " + year;

        // Очищаем таблицу 
        calendarTable.innerHTML = "";

        // Создаем заголовки таблицы для дней недели 
        const headerRow = document.createElement("tr");
        const daysOfWeek = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];
        const classNames = [
            "p-2",
            "border-r",
            "h-10",
            "xl:w-40",
            "lg:w-30",
            "md:w-30",
            "sm:w-20",
            "w-10",
            "xl:text-sm",
            "text-xs",

            // Добавьте классы для каждого дня недели здесь 
        ];
        for (let i = 0; i < daysOfWeek.length; i++) {
            const th = document.createElement("th");
            th.textContent = daysOfWeek[i];

            // Добавляем классы Tailwind CSS 
            th.classList.add(classNames[i]);

            headerRow.appendChild(th);
        }
        calendarTable.appendChild(headerRow);

        // Создаем ячейки для дней месяца 
        const firstDayOfMonth = new Date(year, month, 1);
        const firstDayOfWeek = (firstDayOfMonth.getDay() + 6) % 7; // Учтем смещение 

        // Создаем пустые ячейки в начале месяца, если первый день недели не понедельник 
        let date = 1 - firstDayOfWeek;

        for (let i = 0; i < 6; i++) {
            const row = document.createElement("tr");
            row.classList.add("text-center", "h-12");
            for (let j = 0; j < 7; j++) {
                const cell = document.createElement("td");
                cell.classList.add("border", "p-1", "h-12", "xl:h-40", "xl:w-40", "lg:w-30", "md:w-30", "sm:w-20", "w-10", "overflow-auto", "transition", "cursor-pointer", "duration-500", "ease", "hover:bg-gray-300", "cell");

                if (date <= 0 || date > new Date(year, month + 1, 0).getDate()) {
                    // Заполняем пустые ячейки до начала месяца и после его окончания 
                    cell.textContent = "";
                } else {
                    cell.textContent = date;

                    // Проверяем, является ли текущая ячейка сегодняшней датой
                    const today = new Date();
                    if (date === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
                        // Добавляем стиль или элемент, обозначающий сегодняшнюю дату
                        cell.classList.add("today");
                    }
                    cell.setAttribute("value", year + "-" + (month + 1) + "-" + date);
                }
                date++;
                row.appendChild(cell);
            }
            calendarTable.appendChild(row);
        }
    }

    renderCalendar();

    prevMonthButton.addEventListener("click", function () {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar();
    });

    nextMonthButton.addEventListener("click", function () {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar();
    });

});
