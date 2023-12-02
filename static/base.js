function sendText(){
    console.log(textInput.value);
    fetch('http://localhost:8000/api/send-text', {
        method: 'POST',
        body: new URLSearchParams({
            text: document.getElementById("textInput").value,
            title: document.getElementById("textFilename").value
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