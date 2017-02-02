(function (navigator, $, setColor, audioContext) {
    const BUFF_SIZE = 16384;

    if (!navigator.getUserMedia)
            navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia || navigator.msGetUserMedia;

    if (navigator.getUserMedia){

        navigator.getUserMedia({audio:true}, 
          function(stream) {
              start_microphone(stream);
          },
          function(e) {
            alert('Error capturing audio.');
          }
        );

    } else { alert('getUserMedia not supported in this browser.'); }

    // ---

    function show_some_data(given_typed_array, num_rows_to_display, label) {
        var size_buffer = given_typed_array.length;
        var max_index = num_rows_to_display;
        var colorValues = ['r', 'g', 'b', 'a'];
        var color = {};

        console.log("__________ " + label);
        
        for (var index = 0; index < max_index && index < size_buffer; index += 1) {
            let value = parseInt(Math.max(Math.min((given_typed_array[index] / 100) * 255, 255), 0));
            color[colorValues[index]] = value;
            //console.log(value);
        }
        
        setColor(color);
    }

    function process_microphone_buffer(event) {
        var microphone_output_buffer = event.inputBuffer.getChannelData(0); // just mono - 1 channel for now
        show_some_data(microphone_output_buffer, 4, "from getChannelData");
    }

    function start_microphone(stream){

      var gain_node = audioContext.createGain();
      gain_node.connect( audioContext.destination );

      var microphone_stream = audioContext.createMediaStreamSource(stream);
      microphone_stream.connect(gain_node);

      var script_processor_node = audioContext.createScriptProcessor(BUFF_SIZE, 1, 1);
      script_processor_node.onaudioprocess = process_microphone_buffer;

      microphone_stream.connect(script_processor_node);

      // --- enable volume control for output speakers

      $('#volume').on('change', function() {
          var curr_volume = $(this).val();
          gain_node.gain.value = curr_volume;

          console.log("curr_volume ", curr_volume);
      });

      // --- setup FFT

      var script_processor_fft_node = audioContext.createScriptProcessor(2048, 1, 1);
      script_processor_fft_node.connect(gain_node);

      var analyserNode = audioContext.createAnalyser();
      analyserNode.smoothingTimeConstant = 0;
      analyserNode.fftSize = 2048;

      microphone_stream.connect(analyserNode);

      analyserNode.connect(script_processor_fft_node);

      script_processor_fft_node.onaudioprocess = function() {
        // get the average for the first channel
        var array = new Uint8Array(analyserNode.frequencyBinCount);
        analyserNode.getByteFrequencyData(array);

        // draw the spectrogram
        if (microphone_stream.playbackState == microphone_stream.PLAYING_STATE) {
            show_some_data(array, 4, "from fft");
        }
      };
    }

})(navigator, jQuery, window.setColor, new AudioContext());
