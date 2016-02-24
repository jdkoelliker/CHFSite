$(function() {

  var ptype = $('#id_ptype').val();
  $('#id_creator').toggle(ptype == 'IndividualProduct');
  $('label[for="id_creator"]').toggle(ptype == 'IndividualProduct');
  $('#id_quantity').toggle(ptype == 'BulkProduct');
  $('label[for="id_quantity"]').toggle(ptype == 'BulkProduct');
  $('#id_status').toggle(ptype == 'RentalProduct');
  $('label[for="id_status"]').toggle(ptype == 'RentalProduct');
});

$("#id_ptype").on('change', function() {
  var ptype = $('#id_ptype').val();
  $('#id_creator').toggle(ptype == 'IndividualProduct');
  $('label[for="id_creator"]').toggle(ptype == 'IndividualProduct');
  $('#id_quantity').toggle(ptype == 'BulkProduct');
  $('label[for="id_quantity"]').toggle(ptype == 'BulkProduct');
  $('#id_status').toggle(ptype == 'RentalProduct');
  $('label[for="id_status"]').toggle(ptype == 'RentalProduct');
});
