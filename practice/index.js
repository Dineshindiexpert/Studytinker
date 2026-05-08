window.onload = () => {
    const car = document.querySelector("#car");
    const wheels = document.querySelectorAll(".wheel");

    let position = -200; 
    let rotation = 0;
    let animationId = null;

    function drive() {
        position +=4; 
        rotation += 5;

        if (position > window.innerWidth) {
            position = -200;
        }

        car.style.left = position + "px";

        wheels.forEach(wheel => {
            wheel.style.transform = `rotate(${rotation}deg)`;
        });

        animationId = requestAnimationFrame(drive);
    }

   
    window.startEngine = function() {
        if (!animationId) {
            drive();
            console.log("Engine Started!");
        }
    }
}
