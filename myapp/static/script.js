document.addEventListener("DOMContentLoaded", function () {
    const teamContainers = document.querySelectorAll('.team-photo-container');
    let currentIndex = 0;

    function changeBackground() {
        teamContainers.forEach((container, index) => {
            container.style.opacity = index === currentIndex ? "1" : "0";
            if (index === currentIndex) {
                const photoUrl = container.getAttribute('data-photo-url');
                container.style.backgroundImage = `url(${photoUrl})`;
            }
        });
        currentIndex = (currentIndex + 1) % teamContainers.length;
    }

    changeBackground(); // Начальный вызов
    setInterval(changeBackground, 15000); // Смена каждые 15 секунд
});