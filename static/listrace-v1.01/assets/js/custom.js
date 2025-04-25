$(document).ready(function(){
    "use strict";
    
    /*==================================
    * Author        : "ThemeSine"
    * Template Name : Listrace directory HTML Template
    * Version       : 1.0
    ==================================== */

    /*=========== TABLE OF CONTENTS ===========
    1. Scroll To Top 
    2. slick carousel
    3. welcome animation support
    4. feather icon
    5. counter
    ======================================*/

    // 1. Scroll To Top 
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 600) {
            $('.return-to-top').fadeIn();
        } else {
            $('.return-to-top').fadeOut();
        }
    });
    $('.return-to-top').on('click', function(){
        $('html, body').animate({
            scrollTop: 0
        }, 1500);
        return false;
    });

    // 2. slick carousel
    $(".testimonial-carousel").slick({
        infinite: true,
        centerMode: true,
        autoplay: true,
        slidesToShow: 5,
        slidesToScroll: 3,
        autoplaySpeed: 1500,
        responsive: [
            {
                breakpoint: 1440,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2
                }
            }, 
            {
                breakpoint: 991,
                settings: {
                    slidesToShow: 2,
                    centerMode: false
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });

    // 3. welcome animation support
    $(window).on('load', function(){
        $(".welcome-hero-txt h2, .welcome-hero-txt p").css({'opacity': '0'}).addClass("animated fadeInUp");
        $(".welcome-hero-serch-box").css({'opacity': '0'}).addClass("animated fadeInDown");
    });

    // 4. feather icon
    feather.replace();

    // 5. counter
    $('.counter').waypoint(function() {
        $(this.element).counterUp({
            delay: 10,
            time: 3000
        });
        this.destroy(); // Run once
    }, {
        offset: '80%'
    });

});