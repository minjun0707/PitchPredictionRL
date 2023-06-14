    var on_1b_state = false;
    var on_2b_state = false;
    var on_3b_state = false;

   //1루클릭
   function clickFirstBase() {

    if(on_1b_state == false) {
      on_1b_state = true;
      document.getElementById("on_1b").src = "front-img/base.png"
     
    }
    else {
      on_1b_state = false;
      document.getElementById("on_1b").src = "front-img/base-gray.png"
      
    }
    console.log(on_1b_state)
  }
  //2루클릭
  function clickSecondBase() {
    
    if(on_2b_state == false) {
      on_2b_state = true;
      document.getElementById("on_2b").src = "front-img/base.png"
    }
    else {
      on_2b_state = false;
      document.getElementById("on_2b").src = "front-img/base-gray.png"
    }
    console.log(on_2b_state)
    
  }


  //3루클릭
  function clickThirdBase() {
  

    if(on_3b_state == false) {
      on_3b_state = true;
      document.getElementById("on_3b").src = "front-img/base.png"
    }
    else {
      on_3b_state = false;
      document.getElementById("on_3b").src = "front-img/base-gray.png"
    }
    console.log(on_3b_state)
  }