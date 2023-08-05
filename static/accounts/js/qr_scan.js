 
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  const resultDiv = document.getElementById('result');

  function sendQRCodeData(qrData) {
    // Get the CSRF token from the HTML
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Use jQuery to make an AJAX request to the Django view
    $.ajax({
      url: "{% url 'qreader:qr-data' %}",
      method: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: {
        qr_data: qrData,
      },
      success: function(data) {
        if (data.success) {
          console.log("QR code saved successfully");
           
        } else {
          console.log("Error saving QR code");
        }
      },
      error: function() {
        console.log("AJAX request failed");
      }
    });
  }

  function scanQRCode() {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const code = jsQR(imageData.data, imageData.width, imageData.height);
    if (code) {
      resultDiv.textContent = "QR code detected and decoded: " + code.data;
      // Display the QR code data in the modal body
    $('#qr-code-result').text("QR code detected and decoded: " + code.data);
      $('#exampleModal').modal('show');
       
      sendQRCodeData(code.data);  // Send the QR code data to the Django view
    } else {
      resultDiv.textContent = "Scanning for QR code...";
      // Display the QR code data in the modal body
      //$('#exampleModal').modal('hide');
      setTimeout(scanQRCode, 100);

    }
  }

  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
      video.srcObject = stream;
      video.play();
    })
    .catch(function(err) {
      console.error(err);
    });

  video.addEventListener('play', function() {
    setInterval(scanQRCode, 100);
  });

 
   
  
  
