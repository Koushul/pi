(function ($, tinycolor) {
    
    var color = { r:0, g:0, b:0, a:0 };
    
    var updateColor = function () {
        var $color = $('#color-picker').val();
        color = tinycolor($color).toRgb();
    };
    
    var setColor = function () {
        $.ajax({
            url: '/setColor',
            data: JSON.stringify(color),
            method: 'POST',
    	    dataType: 'json',
    	    contentType: 'application/json',
            success: function(response) {
		let rColor = response.color;
                console.log('Light set to [ R:' + rColor.r + ', G:' + rColor.g + ', B:' + rColor.b + ', A:' + rColor.a + ']');
            }
        });
    };
    
    $(function () {
        var $button = $('#set-color');
        var $picker = $('#color-picker');
        
        $button.on('click', setColor);
        
        $picker.ColorPickerSliders({
            size: 'sm',
            placement: 'right',
            swatches: false,
            order: {
                hsl: 1
            },
            onchange: updateColor
        });
    });
})(jQuery, tinycolor);
