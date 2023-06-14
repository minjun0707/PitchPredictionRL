var strikes = 0
var balls = 0
var outs = 0
//1루클릭
function clickFirstStrike() {
    now_state = strikes
    strikes = 1
   

   
    if(now_state == 2){
        document.getElementById("strike_2").src = "front-img/gray.png"
        strikes = 1
    }
    else if(now_state == 1){
        document.getElementById("strike_1").src = "front-img/gray.png"
        strikes = 0
    }

   else {
    document.getElementById("strike_1").src = "front-img/strike.png"
   }
   console.log(strikes)

    

}


//2루클릭
function clickSecondStrike() {
    now_state = strikes
    strikes = 2

   
    if(now_state == 2){
        document.getElementById("strike_2").src = "front-img/gray.png"
        strikes = 1
    }

   else {
    document.getElementById("strike_1").src = "front-img/strike.png"
    document.getElementById("strike_2").src = "front-img/strike.png"
   }
   console.log(strikes)
   

 

}



//첫번째 볼
function clickFirstBall() {
    now_state = balls
    balls = 1
   
    if(now_state == 3){
        document.getElementById("ball_3").src = "front-img/gray.png"
        document.getElementById("ball_2").src = "front-img/gray.png"
        balls = 1
    }
    else if(now_state == 2){
        document.getElementById("ball_2").src = "front-img/gray.png"
        balls = 1
    }
   else if(now_state == 1) {
        document.getElementById("ball_1").src = "front-img/gray.png"
        balls = 0
   }

   else {
    document.getElementById("ball_1").src = "front-img/ball.png"
   }
   console.log(balls)

   
    
}



//2번째 볼
function clickSecondBall() {
    now_state = balls
    balls = 2
   

    if(now_state == 3){
        document.getElementById("ball_3").src = "front-img/gray.png"
        balls = 2
    }
   else if(now_state == 2) {
        document.getElementById("ball_2").src = "front-img/gray.png"
        balls = 1
   }

   else {
    document.getElementById("ball_1").src = "front-img/ball.png"
    document.getElementById("ball_2").src = "front-img/ball.png"
   }
   console.log(balls)
       



}


//3번째 볼
function clickThirdBall() {
     now_state = balls
     balls = 3
    
     if(now_state == 3){
        document.getElementById("ball_3").src = "front-img/gray.png"
        balls = 2
    }
    else {
        document.getElementById("ball_1").src = "front-img/ball.png"
        document.getElementById("ball_2").src = "front-img/ball.png"
        document.getElementById("ball_3").src = "front-img/ball.png"
    
    }
    console.log(balls)
        
}



function clickFirstOut() {
    now_state = outs
    outs = 1
   

   
    if(now_state == 2){
        document.getElementById("out_2").src = "front-img/gray.png"
        outs = 1
    }
    else if(now_state == 1){
        document.getElementById("out_1").src = "front-img/gray.png"
        outs = 0
    }

   else {
    document.getElementById("out_1").src = "front-img/out.png"
   }
   console.log(outs)

    

}


//2루클릭
function clickSecondOut() {
    now_state = outs
    outs = 2

   
    if(now_state == 2){
        document.getElementById("out_2").src = "front-img/gray.png"
        outs = 1
    }

   else {
    document.getElementById("out_1").src = "front-img/out.png"
    document.getElementById("out_2").src = "front-img/out.png"
   }
   console.log(outs)
   

 

}