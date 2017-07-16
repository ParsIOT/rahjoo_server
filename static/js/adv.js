//بهره تو خود فایل اصلی ناحیه ها رو با همین درخوایت ابتدایی بگیریم. بفیه رو وقتی انتخاب می کنیم تبلیغ رو فقط هایلایت کنیم.


$(document).ready(function () {
    var $row;
    var allRecAreas;
    $('.adv_edit_button').click(function () {
        $row = $(this).closest("tr");
        var adv_name = $row.find("td:nth-child(1)").text().trim();
        var adv_text = $row.find("td:nth-child(2)").text().trim();
        var price = $row.find("td:nth-child(3)").text().trim();
        $('#modal_advertisement_name').val(adv_name);
        $('#modal_advertisement_text').val(adv_text);
        $('#modal_total_price').html(price);

        //get advertisements areas from db
        $.ajax({
            url: '../../../ajax/getAdvertisementsAreas',
            data: {
                'adv_name': adv_name,
                'adv_text': adv_text
            },
            dataType: 'json',
            success: function (data) {
                selected_sections = data['selected_sections'];

            }
        });
        $('#myModal').modal('show');
    });

});

