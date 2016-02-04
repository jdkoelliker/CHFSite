$(function() {

  $('#loginbutton').click(function(){

    $.loadmodal({
      url: '/account/login/',
      id: 'loginmodal',
      title: 'Login to CHF!',
      width: '400px',
    });
  });
});

$(function() {

  $('#createaccountbutton').click(function(){

    $.loadmodal({
      url: '/account/createaccount/',
      id: 'createaccountmodal',
      title: 'Create an account!',
      width: '400px',
    });
  });
});
