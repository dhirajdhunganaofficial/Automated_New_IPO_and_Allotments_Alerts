const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
console.log("timezone")
console.log(timezone)

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        menuIcon.classList.remove('bx-x');
        navbar.classList.remove('active');
    });
});

window.addEventListener('scroll', () => {
    let top = window.scrollY;

    navLinks.forEach(link => link.classList.remove('active'));

    sections.forEach(sec => {
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.id;

        if (top >= offset && top < offset + height) {

            const activeLink = document.querySelector(
                `header nav a[href="#${id}"]`
            );

            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    });
});
