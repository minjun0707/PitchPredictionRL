import numpy as np

def predict(best_model,input,ptm_list) :
    # X=data[['balls', 'strikes','on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', 'pitch_number', 'score_difference', 'pre1', 'pre2', 'pre3', 'stand_L', 'stand_R']]  # Features
    # 위 순서대로 input값 저장


    result = best_model.predict(input.reshape(1,-1))

    for i in range (0, len(ptm_list)):
        if(result[0] == i+1):
            value = ptm_list[i]
            print(value)
            break

    probability = best_model.predict_proba(input.reshape(1,-1))
    print(probability)
    print(np.max(probability))
    return value, np.max(probability)