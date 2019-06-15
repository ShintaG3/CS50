$(document).ready(function() {


    // /* For the sticky navigation */
    // $('.js--section-features').waypoint(function(direction) {
    //     if (direction == "down") {
    //         $('nav').addClass('sticky');
    //     } else {
    //         $('nav').removeClass('sticky');
    //     }
    // }, {
    //   offset: '60px;'
    // });


    /* Scroll on buttons */
    $('.js--scroll-to-plans').click(function () {
       $('html, body').animate({scrollTop: $('.js--section-plans').offset().top}, 1000);
    });

    $('.js--scroll-to-start').click(function () {
       $('html, body').animate({scrollTop: $('.js--section-features').offset().top}, 1000);
    });


    /* Navigation scroll */
    $(function() {
      $('a[href*=#]:not([href=#])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 1000);
            return false;
          }
        }
      });
    });

    //
    // /* Animations on scroll */
    // $('.js--wp-1').waypoint(function(direction) {
    //     $('.js--wp-1').addClass('animated fadeIn');
    // }, {
    //     offset: '50%'
    // });
    //
    // $('.js--wp-2').waypoint(function(direction) {
    //     $('.js--wp-2').addClass('animated fadeInUp');
    // }, {
    //     offset: '50%'
    // });
    //
    // $('.js--wp-3').waypoint(function(direction) {
    //     $('.js--wp-3').addClass('animated fadeIn');
    // }, {
    //     offset: '50%'
    // });
    //
    // $('.js--wp-4').waypoint(function(direction) {
    //     $('.js--wp-4').addClass('animated pulse');
    // }, {
    //     offset: '50%'
    // });

    // $('.js--nav-icon').click(function() {
    //   $('.js--nav-icon').slideToggle(200);
    // });
    //
    /* Mobile navigation */
    // $(window).resize(function(){
    //   var windowWidth = $(window).width();
    //   var nav = $('.js--main-nav');
    //   console.log(windowWidth);
    //   if(windowWidth > 750){
    //     nav.css({
    //       "display":"block"
    //     });
    //   }else{
    //     nav.css({
    //       "display":"none"
    //     });
    //   };
    // });

    $('.js--nav-icon').click(function() {

      var nav = $('.js--main-nav');
      var icon = $('.js--nav-icon ion-icon');

      nav.slideToggle(200);
      var name = icon.prop("name");

      if(name=="menu") {
        icon.attr("name", "close");
      }else{
        icon.attr("name", "menu");
      };
    });





    //   }
    //     //
    //     //
    //     // if (icon.hasClass('ion-navicon-round')) {
    //     //     icon.addClass('ion-close-round');
    //     //     icon.removeClass('ion-navicon-round');
    //     // } else {
    //     //     icon.addClass('ion-navicon-round');
    //     //     icon.removeClass('ion-close-round');
    //     // }
    //   });
});
