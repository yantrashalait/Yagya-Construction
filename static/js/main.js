(function($) {
  'use strict'; 
$(document).ready(function(){

	/*---------------------------------/
            Magnific popup-video JS
    ---------------------------------*/

    $('.about__video__play').magnificPopup({ 
          type: 'iframe',
          iframe: {
              markup: '<div class="mfp-iframe-scaler">'+
                  '<div class="mfp-close"></div>'+
                  '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
                  '<div class="mfp-title">Some caption</div>'+
                  '</div>',
              patterns: {
                  youtube: {
                      index: 'youtube.com/', 
                      id: 'v=',
                      src: 'https://www.youtube.com/watch?v=2YDjL0cHjGc'
                  }
              }
          }
          // other options
      });
     /*---------------------------------/
            Magnific popup-video JS
    ---------------------------------*/


$('.projects__imgs__slide').owlCarousel({
        loop: false,
        rewind: true,
        responsiveClass: true,
        nav: true,
        smartSpeed: 500,
        dots: false,
        navText: ['<span class="left__arrow"></span>', '<span class="right__arrow"></span>'],
        responsive : {
            992 : {
                items: 1
            },
    
            768 : {
                items: 1
            },
            
            576 : {
                items: 1
            },
            
            0 : {
                items: 1
            }
        }
    });
});// document ready





})(window.jQuery);   
