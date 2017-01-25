(function ($) {
    
    var color = { r:255, g:255, b:255, a:1 };
    
    var updateColor = function (newColor) {
        color = newColor;
    };
    
    var setColor = function () {
        $.ajax({
            url: '/setColor',
            data: JSON.stringify(color),
            method: 'POST',
    	    dataType: 'json',
    	    contentType: 'application/json',
            success: function(response) {
		        let c = response.color;
                console.log('Light set to [ R:' + c.r + ', G:' + c.g + ', B:' + c.b + ', A:' + c.a + ']');
            }
        });
    };
    
    $(function () {
        var $button = $('#set-color');
        var $picker = $('#color-picker');
        
        $button.on('click', setColor);
        
        $picker.ColorPickerSliders({
            color: 'rgb(255, 255, 255)',
            size: 'default',
            placement: 'right',
            animation: true,
            swatches: false,
            order: {
                rgb: 1,
                opacity: 2
            },
            onchange: function (container, color) {
                updateColor(color.tiny.toRgb());
            }
        });
    });
})(jQuery);
