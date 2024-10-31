document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('images-container');
    const images = container.getAttribute('data-images').split(',');

    console.log('Images:', images);  // Отладочный вывод списка изображений

    let currentIndex = 0;
    const heroSection = document.querySelector('.hero');

    function changeBackground() {
        if (images.length > 0) {
            console.log('Changing to:', images[currentIndex]);  // Отладочный вывод
            heroSection.style.backgroundImage = `url('/media/${images[currentIndex]}')`;
            currentIndex = (currentIndex + 1) % images.length;
        }
    }

    setInterval(changeBackground, 5000);
    changeBackground();
});