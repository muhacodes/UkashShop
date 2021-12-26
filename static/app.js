$(document).ready(function(){
    ProductDeleteConfirm();
    CloseAlertAfterSeconds();
});

function ProductDeleteConfirm(){
    $('#delete_product').click(function(){
        var id = $(this).data('id');

        $('#confirm_delete_product').val(id);
    });
}

function CloseAlertAfterSeconds(){
    $("#success-alert").fadeTo(3000, 1000).slideUp(1000, function(){
        $("#success-alert").slideUp(1000);
    });
}
