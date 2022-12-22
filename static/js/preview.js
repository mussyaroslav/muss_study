function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#setting__profile__photo')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function readURL1(input) {
    if (input.files && input.files[0]) {
        var reader1 = new FileReader();

        reader1.onload = function (e) {
            $('#setting__profile__photo__background')
                .attr('src', e.target.result);
        };

        reader1.readAsDataURL(input.files[0]);
    }
}