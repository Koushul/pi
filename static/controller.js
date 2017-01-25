(function ($) {
    
    var setColor = function () {
        var color = [ 127, 127, 127, 127 ];
        
        $.ajax({
            url: '/setColor',
            data: JSON.stringify(color),
            method: 'POST',
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
