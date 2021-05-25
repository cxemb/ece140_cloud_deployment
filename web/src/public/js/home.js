document.addEventListener("DOMContentLoaded", (event) => {

    var theSnapshots = document.querySelector("#guest");

    theSnapshots.addEventListener("click", (event) => {
        fetch(theURL)
            .then(response => response.json())
            .then(function() {
              console.log('NEW GUEST INCOMING');
              buttAlert();
              });
    });

    /*var inpButt = document.querySelector("input[name='guestButton']");*/

    /*var inpButt = document.querySelector("input[name='guestButton']");*/

    /*inpButt.addEventListener("click", function(event) {*/
        
    /*});*/
});