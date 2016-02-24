$( document ).ready(function() {
    $(".Delete").click(function(event) {
        //Prevents href from executing
        event.preventDefault();

        //set variable equal to href link
        var deleteLink = $( this ).attr( "href" );
        //set href on new button
        $( '#confirm_delete_button' ).attr( "href", deleteLink );
        //show modal on click
        $( '#delete_modal').modal( 'show' );
    });
});

$('.refresh_button').click(function(e) {
  e.preventDefault();
  var href = $(this).attr("href");
    $(this).siblings('.quantity').load(href);
});
