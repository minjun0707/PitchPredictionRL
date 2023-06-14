import numpy as np
from flask import Flask, jsonify
from flask import request
import json
import joblib

import parse
import predictResultDto
from reinForce import rfStart

app = Flask(__name__)


# 테스트를 위한 기본페이지
@app.route("/")
def basicPage():
    return "<h1>Flask Server<h1>"


# 스프링 서버에서 POST 방식으로 넘어오는 요청을 처리
# URL : /api/flask/pitch-detection
@app.route('/api/flask/pitch-detection', methods=['POST'])
def pitchDetection():
    # 스프링 서버에서 request가 올바르게 왔는지 확인  (True / false)
    print("request", request.is_json)

    # request body를 json으로 변환
    params = request.get_json()

    name = params['name']
    balls = params['balls']
    strikes = params['strikes']
    on_3b = params['on_3b']
    on_2b = params['on_2b']
    on_1b = params['on_1b']
    outs_when_up = params['outs_when_up']
    inning = params['inning']
    pitch_number = params['pitch_number']
    score_difference = params['score_difference']
    pre1 = params['pre1']
    pre2 = params['pre2']
    pre3 = params['pre3']
    stand_L = params['stand_L']
    stand_R = params['stand_R']

    # name = params['name']
    # balls = params['balls']
    # strikes = params['strikes']
    # on_1b = params['on_1b']
    # outs_when_up = params['outs_when_up']
    # inning = params['inning']
    # pitch_number = params['pitch_number']
    # score_difference = params['score_difference']
    # pre1 = params['pre1']
    # pre2 = params['pre2']
    # pre3 = params['pre3']
    # stand_L

    input = np.array([balls, strikes, on_3b, on_2b, on_1b, outs_when_up, inning, pitch_number,
                      score_difference, pre1, pre2, pre3, stand_L, stand_R])

    value = parse.readCsv(name)

    if value == "0" :
        print("test 모델")
        model = joblib.load('model/test.pkl')
    else :
        print(int(float(value)))
        fileName = "model/" + str(int(float(value))) + ".pkl"
        model = joblib.load(fileName)


    # if name == "Carlos Rodon":
    #     model = joblib.load('model/607074.pkl')
    #
    # elif name == "Tyler Glasnow":
    #     model = joblib.load('model/607192.pkl')
    #     print("------------" + name + " ----------------")
    #
    # elif name == "Josh Hader":
    #     model = joblib.load('model/623352.pkl')
    #
    # else:
    #     model = joblib.load('model/test.pkl')



    result = model.predict(input.reshape(1, -1))

    # 각 구종별 확률 확인
    probability = model.predict_proba(input.reshape(1, -1))
    print(probability)

    predictedResult = result[0]
    print(predictedResult)
    if result[0] == 1:
        predictedResult = "직구"
    elif result[0] == 2:
        predictedResult = "커브"
    elif result[0] == 3:
        predictedResult = "체인지업"
    elif result[0] == 4:
        predictedResult = "슬라이더"
    elif result[0] == 5:
        predictedResult = "싱커"

    probability = model.predict_proba(input.reshape(1, -1))

    predictResultDto.setPredictResult(predictedResult)
    action = rfStart()

    # 최대 확률을 가진 구종의 확률 출력
    # predictedResult = predictedResult + ":" + str(round(np.max(probability), 3))

    print("pitchType", predictedResult)
    print("probability", str(round(np.max(probability), 3)))
    print("action", action)
    # 연산 후 결과를 key 와 value 형태인 json으로 변경
    # 추후 실제 연산 결과 저장될 예정
    data = {
        'pitchType': predictedResult,
        'probability': str(round(np.max(probability), 3)),
        'action': str(action)
    }

    # Python의 객체를 JSON 문자열로 변환
    json_data = json.dumps(data, ensure_ascii=False)

    # 스프링 서버로 요청 전송
    return json_data


#안쓰는
@app.route('/api/flask/reinforcement', methods=['POST'])
def reinforcement():
    # 스프링 서버에서 request가 올바르게 왔는지 확인  (True / false)
    print("request", request.is_json)

    # request body를 json으로 변환
    params = request.get_json()

    balls = params['balls']

    data = {
        'result': '직구 78%'
    }

    # Python의 객체를 JSON 문자열로 변환
    json_data = json.dumps(data, ensure_ascii=False)

    # 스프링 서버로 요청 전송
    return json_data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
