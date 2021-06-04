document.addEventListener("DOMContentLoaded",(event) => {
    console.log('new content!')
    function addGuest() {
        var gFName = document.getElementById("first_name").value;
        var gLName = document.getElementById("last_name").value;
        var gEmail = document.getElementById("email").value;
        var gComment = document.getElementById("comment").value;

        var gNew =  {gFName, gLName, gEmail, gComment};
        
        console.log(gNew);
        
        fetch('http://localhost/add_guest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(gNew),
        })
        .then(response => response.json())
        .then(gNew => {
        console.log('Success:', gNew);
        })
        .catch((error) => {
        console.error('Error:', error);
        });
    }
    var submitGuest = document.getElementById("guest");
    submitGuest.addEventListener('click', addGuest);    
});