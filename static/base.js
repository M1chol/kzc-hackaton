function sendText(){
    console.log(textInput.value);
    var text_val = document.getElementById("textInput").value;
    var title_val = document.getElementById("textFilename").value;
    // https://www.slashcoding.com/wp-content/uploads/2014/03/page-loader.gif
    document.getElementById("textbox").innerHTML = '<img src="https://cdn.dribbble.com/users/2882885/screenshots/7861928/media/a4c4da396c3da907e7ed9dd0b55e5031.gif" alt="Animated GIF">';
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
    document.getElementById("textbox").innerHTML = response.html;

}