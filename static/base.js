var textInput = document.getElementById("textInput")
var textTitle = document.getElementById("textFilename")
var ip = location.host;

function sendText(){
    fetch('http://localhost:8000/api/send-text', {
        method: 'POST',
        body: new URLSearchParams({
            text: textInput.value,
            title: textTitle.value
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error sending text:', error);
    });
}