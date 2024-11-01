    const about = document.querySelector('.about');
    const imagesContainer = about.querySelector('#images-container');
    let images = [];

    if (imagesContainer) {
        images = imagesContainer.dataset.images.split(',').filter(Boolean);
    }

    let currentIndex = 0;

    function createImageElement(src) {
        const img = document.createElement('img');
        img.src = src;
        img.classList.add('about-background');
        return img;
    }

    function showNextImage() {
        if (images.length === 0) return;

        const nextIndex = (currentIndex + 1) % images.length;
        const nextImage = createImageElement(images[nextIndex]);

        setTimeout(() => {
            // Add the new image to the DOM
            about.appendChild(nextImage);

            // Add the 'active' class to the new image
            nextImage.classList.add('active');

            // Find the current active image (excluding the last child to avoid the new image)
            const currentImage = about.querySelector('.about-background.active:not(:last-child)');

            if (currentImage) {
                // Remove the 'active' class from the current image
                currentImage.classList.remove('active');

                // Remove the current image from the DOM after a delay
                setTimeout(() => {
                    currentImage.remove();
                },000);
            }

            // Update the current index
            currentIndex = nextIndex;
        }, 100);
    }

    // Display the initial image
    if (images.length > 0) {
        const initialImage = createImageElement(images[0]);
        initialImage.classList.add('active');
        about.appendChild(initialImage);

        // Change image every 15 seconds
        setInterval(showNextImage, 15000);
    }
});

    // Initial image
    if (images.length > 0) {
        const initialImage = createImageElement(images[0]);
        initialImage.classList.add('active');
        about.appendChild(initialImage);

        // Change image every 15 seconds
        setInterval(showNextImage, 15000);
    }
});

// document.addEventListener('DOMContentLoaded', function() {
//     const container = document.getElementById('images-container');
//     const images = container.getAttribute('data-images').split(',');
//
//     console.log('Images:', images);  // Отладочный вывод списка изображений
//
//     let currentIndex = 0;
//     const heroSection = document.querySelector('.hero');
//
//     function changeBackground() {
//         if (images.length > 0) {
//             console.log('Changing to:', images[currentIndex]);  // Отладочный вывод
//             heroSection.style.backgroundImage = `url('/media/${images[currentIndex]}')`;
//             currentIndex = (currentIndex + 1) % images.length;
//         }
//     }
//
//     setInterval(changeBackground, 5000);
//     changeBackground();
// });