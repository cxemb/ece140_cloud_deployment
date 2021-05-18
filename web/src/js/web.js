document.addEventListener("DOMContentLoaded", (event) => {

    document.addEventListener("click",function(event) {
        console.log("click!");

        var buttPlan = document.querySelector(".bPlan");
        var P = document.getElementById("planDiv");
        
        var buttLive = document.querySelector(".bLive");
        var L = document.getElementById("liveDiv");

        // show plan stuff when click on plan button --------
        function showPlan() {
            P.style.display = "block";
        }

        function hidePlan() {
            P.style.display = "none";
        }

        buttPlan.addEventListener("click",function(event) {
            showPlan();
            console.log("showing plan");
            hideLive();
            console.log("hiding live");
        });

        // show live stuff when click on live button --------
        function showLive() {
            L.style.display = "block";
        }

        function hideLive() {
            L.style.display = "none";
        }

        buttLive.addEventListener("click",function(event) {
            showLive();
            console.log("showing live");
            hidePlan();
            console.log("hiding plan");
        });
    });

});