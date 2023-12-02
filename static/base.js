function sendText(){
    console.log(textInput.value);
    var text_val = document.getElementById("textInput").value;
    var title_val = document.getElementById("textFilename").value;
    document.getElementById("texttext").innerHTML = '<img src="https://www.slashcoding.com/wp-content/uploads/2014/03/page-loader.gif" alt="Animated GIF">';
    fetch('http://localhost:8000/api/send-text', {
        method: 'POST',
        body: new URLSearchParams({
            text: text_val,
            title: title_val
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.raw);
        displayText(data);
    })
    .catch(error => {
        console.error('Error sending text:', error);
    });
    
}

function displayText(response){
    document.getElementById("texttext").innerHTML = response.html;

}