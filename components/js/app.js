// Scroll Section Active Link

// const sections = document.querySelectorAll('section[id]')

// const scrollActive = () => {
//     const scrollY = window.pageYOffset

//     sections.forEach(current =>{
//         const sectionHeight = current.offsetHeight
//         const sectionTop = current.offsetTop - 50;
//         sectionId = current.getAttribute('id')

//         if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
//             document.querySelector('.nav-menu  [href*=' + sectionId + ']').classList.add('active-links')
//         }else{
//             document.querySelector('.nav-menu  [href*=' + sectionId + ']').classList.remove('active-links')
//         }
//     })
// }

// window.addEventListener('scroll', scrollActive);



// Show Scroll Top
function scrollTop(){
    const scrollTop = document.getElementById('scroll-top');
    // When the scroll is higher than 560 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if(this.scrollY >= 160) scrollTop.classList.add('show-scroll'); else scrollTop.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollTop) 


// Scroll Animation
const sr = ScrollReveal({
    origin: 'top',
    distance: '30px',
    duration: 2000,
    reset: true
});

sr.reveal(`.hero-text, .hero-img, .about__data, .about__img, 
           .services__content, .carousel-inner, .form-form, .menu__content, .section-title`, {
    interval: 200
});;