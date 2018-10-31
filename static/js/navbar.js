$(document).ready(function() {
  var stickyNavTop = $('.navbar').offset().top;
  // var scrollBottom = $(window).scrollBottom();

  var stickyNav = function(){
    // var scrollBottom = $(window).scrollBottom();
    var scrollTop = $(window).scrollTop();

    if (scrollTop > stickyNavTop) {
      $('.navbar').addClass('sticky');
      $('.topform').hide()
    }
    else {
      $('.navbar').removeClass('sticky');
      $('.topform').show()
    }
  };

  stickyNav();

  $(window).scroll(function() {
    stickyNav();
  });
});
