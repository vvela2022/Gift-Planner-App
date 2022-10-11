
$(document).ready(function(){
    $('.carousel.carousel-slider').carousel({
        fullWidth:true,
        indicators:true,
    }).height(700);

    autoplay();

    function autoplay(){
        $('.carousel').carousel('next')
        setTimeout(autoplay, 5000)
    } 
});

