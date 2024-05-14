
(function($) {

   "use strict";

   $(window).stellar({
   responsive: true,
   parallaxBackgrounds: true,
   parallaxElements: true,
   horizontalScrolling: false,
   hideDistantElements: false,
   scrollProperty: 'scroll'
 });


   var fullHeight = function() {

       $('.js-fullheight').css('height', $(window).height());
       $(window).resize(function(){
           $('.js-fullheight').css('height', $(window).height());
       });

   };
   fullHeight();


   // Scrollax
  $.Scrollax();



  // Burger Menu
   var burgerMenu = function() {

       $('body').on('click', '.js-fh5co-nav-toggle', function(event){

           event.preventDefault();

           if ( $('#ftco-nav').is(':visible') ) {
               $(this).removeClass('active');
           } else {
               $(this).addClass('active');	
           }

           
           
       });

   };
   burgerMenu();


   var onePageClick = function() {

       $(document).on('click', '#ftco-nav a[href^="#"]', function (event) {
       event.preventDefault();

       var href = $.attr(this, 'href');

       $('html, body').animate({
           scrollTop: $($.attr(this, 'href')).offset().top - 70
       }, 500, function() {
           // window.location.hash = href;
       });
       });

   };

   onePageClick();
   

   // scroll
   var scrollWindow = function() {
       $(window).scroll(function(){
           var $w = $(this),
                   st = $w.scrollTop(),
                   navbar = $('.ftco_navbar'),
                   sd = $('.js-scroll-wrap');

           if (st > 150) {
               if ( !navbar.hasClass('scrolled') ) {
                   navbar.addClass('scrolled');	
               }
           } 
           if (st < 150) {
               if ( navbar.hasClass('scrolled') ) {
                   navbar.removeClass('scrolled sleep');
               }
           } 
           if ( st > 350 ) {
               if ( !navbar.hasClass('awake') ) {
                   navbar.addClass('awake');	
               }
               
               if(sd.length > 0) {
                   sd.addClass('sleep');
               }
           }
           if ( st < 350 ) {
               if ( navbar.hasClass('awake') ) {
                   navbar.removeClass('awake');
                   navbar.addClass('sleep');
               }
               if(sd.length > 0) {
                   sd.removeClass('sleep');
               }
           }
       });
   };
   scrollWindow();

   

})(jQuery);

