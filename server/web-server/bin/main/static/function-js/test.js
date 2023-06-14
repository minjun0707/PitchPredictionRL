function test(){
    console.log("name :" + document.getElementById("input").value)
    console.log("score_difference :" + (document.getElementById("score_a").value - document.getElementById("score_b").value))
    console.log("on_1b_state :" + on_1b_state)
    console.log("on_2b_state :" + on_2b_state)
    console.log("on_3b_state :" + on_3b_state)
    console.log("inning :" + count)
    console.log("stand :" + $('input[name="stand"]:checked').val())
    console.log("strikes :" + strikes)
    console.log("balls :" + balls)
    console.log("outs_when_up :" + outs)
    console.log("pitch_number :" + document.getElementById("pitch_number").value)
    console.log("pre1 :" + document.getElementById("pre1").value)
    console.log("pre2 :" + document.getElementById("pre2").value)
    console.log("pre3 :" + document.getElementById("pre3").value)
}

// function btnClick(){
//     console.log("click")
// }
    