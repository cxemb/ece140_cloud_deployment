document.addEventListener("DOMContentLoaded", (event) => {

    document.addEventListener("click",function(event) {
        console.log("click!");

        // if command == takeoff, land: don't need arg
        if(event.target.matches(".noArg")) {
            fetch('http://localhost:/templates/cv.html')
            .then(response => response.json())
            .then(function(response) {
                console.log(event.target.id);
            });
        }
    });

});