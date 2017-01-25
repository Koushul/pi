(function ($) {
    
    var setColor = function () {
        var color = {r:127, g:127, b:127, a:127 };

        $.ajax({
            url: '/setColor',
            data: JSON.stringify(color),
            method: 'POST',
	    dataType: 'json',
	    contentType: 'application/json',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    };
    
    $(function () {
        var $button = $('#set-color');
        
        $button.on('click', setColor);
    });
})(jQuery);
