function modalResult(pitchType,action) {
    
    if(pitchType == "직구") {
        pitchType ="FastBall"
    }
    else if(pitchType == "커브") {
        pitchType ="CurveBall"
    }
    else if(pitchType == "체인지업") {
        pitchType ="ChangeUp"
    }
    else if(pitchType == "슬라이더") {
        pitchType = "Slider"
    }
    else if(pitchType == "싱커") {
        pitchType = "Sinker"
    }
    document.getElementById("pitchType").innerHTML = pitchType;


    if(action == 0) {
        document.getElementById("actionImg").src = "front-img/hit-remove.png"
        document.getElementById("action").innerHTML = "Hit";

    } else if(action == 1) {
        document.getElementById("actionImg").src = "front-img/cut-remove.png"
        document.getElementById("action").innerHTML = "Cutting";
    } else if(action == 2) {
        document.getElementById("actionImg").src = "front-img/notHit.png"
        document.getElementById("action").innerHTML = "Not Hit";
    }
}