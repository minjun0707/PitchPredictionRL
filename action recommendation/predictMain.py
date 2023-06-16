import joblib
import numpy as np

def main():
    # model 불러오기
    model = joblib.load('test.pkl')

    # input 목록
    balls = 3
    strikes = 0
    on_3b = 0
    on_2b = 0
    on_1b = 0
    outs_when_up = 2
    inning = 6
    pitch_number = 4
    score_difference = 0
    pre1 = 1
    pre2 = 1
    pre3 = 2
    stand_L = 1
    stand_R = 0

    # input을 numpy array로 변환
    input = np.array([balls, strikes, on_3b, on_2b, on_1b, outs_when_up, inning,
                      pitch_number, score_difference, pre1, pre2, pre3, stand_L, stand_R])

    # 예측
    result = model.predict(input.reshape(1, -1))

    # 결과 출력
    predictedResult = result[0]
    print(predictedResult)
    if result[0] == 1 :
        predictedResult ="직구"
    elif result[0] == 2:
        predictedResult = "커브"
    elif result[0] == 3:
        predictedResult = "체인지업"
    elif result[0] == 4:
        predictedResult = "슬라이더"
    elif result[0] == 5:
        predictedResult = "싱커"

    # 각 구종별 확률 확인
    probability = model.predict_proba(input.reshape(1, -1))

    # 최대 확률을 가진 구종의 확률 출력
    print(predictedResult + ":",round(np.max(probability), 3))

    return predictedResult






if __name__ == '__main__':
    main()