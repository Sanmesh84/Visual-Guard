
var dropdown=document.getElementById('carcompany');
    var selectedcar;
    dropdown.addEventListener('change',function(event){
        selectedcar=event.target.value;
        console.log(selectedcar);
    })




function uploadImage() {
    var outputdata={};
    var flag1=false;
    var flag2=false;
    var fileInput = document.getElementById('fileInput');
    var seatimage=document.getElementById('seatimage');

    if (fileInput.files.length > 0) {
        var formData = new FormData();
        formData.append('img', fileInput.files[0]);
        formData.append('seatimg', seatimage.files[0]);
        formData.append('cartype',selectedcar)
        // Make a POST request to your backend server with CORS headers
        axios.post('http://127.0.0.1:5000/getprediction', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Access-Control-Allow-Origin': '*'  // Allow requests from all origins (for demonstration purposes)
                // Consider using a specific origin or handling CORS more securely in a production environment
            }
        })
        .then(response => {
            // Handle the response from the server
            flag1=true
            outputdata={...outputdata,...response.data}
            if(flag1 && flag2){
                window.location.href="/output.html?result="+encodeURIComponent(JSON.stringify(outputdata))
            }

            console.log('Server Response:', response.data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
        axios.post('http://127.0.0.1:5000/getdamage', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Access-Control-Allow-Origin': '*'  // Allow requests from all origins (for demonstration purposes)
                // Consider using a specific origin or handling CORS more securely in a production environment
            }
         })
         .then(response => {
            // Handle the response from the server
            flag2=true
            outputdata={...outputdata,...response.data}
            if(flag1 && flag2){
                window.location.href="/output.html?result="+encodeURIComponent(JSON.stringify(outputdata))
            }
             console.log('Server Response:', response.data);
         })
         .catch(error => {
             console.error('Error:', error);
         });
     } else {
        alert('Please select an image to upload.');
    }
   }

