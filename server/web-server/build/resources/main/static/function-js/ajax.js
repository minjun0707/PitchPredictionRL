function ajax() {
  $.ajax({
      type: 'post',
      contentType: 'application/json',

      //production url
      url: 'https://pitchingbaseball.duckdns.org/api/pitch-detection',

      //local url
      //url: 'http://localhost:8080/api/pitch-detection',
      data: JSON.stringify ({
          "name" :document.getElementById("input").value,
          "score_difference" : (document.getElementById("score_a").value - document.getElementById("score_b").value),
          "on_1b" : on_1b_state,
          "on_2b" : on_2b_state,
          "on_3b" :on_3b_state,
          "inning" : count,
          "stand" : $('input[name="stand"]:checked').val(),
          "strikes" : strikes,
          "balls" : balls,
          "outs_when_up" : outs,
          "pitch_number" : document.getElementById("pitch_number").value,
          "pre1" : document.getElementById("pre1").value,
          "pre2" : document.getElementById("pre2").value,
          "pre3" : document.getElementById("pre3").value
      }),
      dataType: 'text',
      error: function (xhr, status, error) {
          alert(error + "error");
      },
      success: function (json) {
          const obj = JSON.parse(json);
          console.log("서버로부터 결과를 받았습니다.")
          console.log(obj.pitchType +" " + obj.probability + " " + obj.action)
          test();
          modalResult(obj.pitchType,obj.action);
          $('#resultText').val(obj.pitchType +" " + obj.probability + " " + obj.action);
      }
  });

}
