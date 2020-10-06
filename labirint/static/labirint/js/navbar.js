document.querySelectorAll('.nav-link').forEach(elem => {
    if (elem.getAttribute('href') === document.location.pathname) {
        elem.classList.add('active')
    }
});