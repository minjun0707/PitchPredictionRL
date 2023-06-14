from pybaseball import statcast_pitcher

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

read_df = pd.read_csv(r'ID.csv')

score_list_2 = []
score_list_3 = []
score_list_4 = []
score_list_5 = []
score_list_6 = []
score_list_7 = []
score_list_8 = []

for i in range (0, read_df.shape[0]):
    print('\n\n---------------------------------\n\n')
    player_id = read_df["MLBID"][i]
    player_name = read_df["MLBNAME"][i]

    print("[Iteration " + str(i) + "]\n")
    print("Current player id: " + str(player_id) + ", name: " + str(player_name) + "\n")

    # load pitch data
    df = statcast_pitcher('2020-05-01', '2023-10-30', player_id)

    # preprocsseing

    # extracting columns that are only wanted
    df = df[['pitch_type', 'stand', 'balls', 'strikes',  'on_3b',  'on_2b', 'on_1b', 'outs_when_up', 'inning',
    'pitch_number', 'bat_score', 'fld_score']]

    # base ruuner mapping
    for i in range (0, len(df["on_1b"].axes[0])): #on the first base
        if df.loc[i,"on_1b"] > 0: # if there is any value, map it to 1
            df.at[i,"on_1b"] = 1.0
        else: # if not, to 0
            df.at[i,"on_1b"] = 0.0
            
    for i in range (0, len(df["on_2b"].axes[0])): #on the second base
        if df.loc[i,"on_2b"] > 0: # if there is any value, map it to 1
            df.at[i,"on_2b"] = 1.0
        else: # if not, to 0
            df.at[i,"on_2b"] = 0.0
            
    for i in range (0, len(df["on_3b"].axes[0])): #on the third base
        if df.loc[i,"on_3b"] > 0:# if there is any value, map it to 1
            df.at[i,"on_3b"] = 1.0
        else: # if not, to 0
            df.at[i,"on_3b"] = 0.0

    # drop rows with nan values
    df = df.dropna()

    # create new feature 'score_difference' and drop columns un-needed
    df["score_difference"] = df["fld_score"] - df["bat_score"]
    df.drop(["fld_score", "bat_score"], axis=1, inplace=True)

    # get a pitch type of the pitcher
    pt_list = df['pitch_type'].unique()

    # print pitch arsenal percentage
    print("Original pitch aresnal\n")
    print(df['pitch_type'].value_counts(normalize=True) * 100)

    # drop pitch types that has been thrown less than 3%
    pt_filter = df.pitch_type.value_counts(normalize=True) > 0.03
    pt_index = pt_filter[pt_filter.values == True].index
    df = df[df.pitch_type.isin(list(pt_index))]

    # let's see how it has changed
    print("\n\nHow it has changed\n")
    ptm_list = df['pitch_type'].unique()
    print(ptm_list)
    print(df['pitch_type'].value_counts(normalize=True) * 100)

    # mapping pitch_type with index of'pt_list'
    for i in range (0, len(ptm_list)):
        if i > len(ptm_list): break
        df['pitch_type'].mask(df['pitch_type'] == ptm_list[i] , i+1 , inplace=True)

    # create temporary dataframe for previous pitch tendency dataframe
    pre_df = pd.DataFrame(0, index=np.arange(df.shape[0]), columns=['pre1', 'pre2', 'pre3'])

    # to prevent 'key error'
    # the iteration will be made based on the number of the rows in 'pre_df', which is same as 'df'
    num = pre_df.shape[0]

    # concatenate these two dataframes
    df = pd.concat([df, pre_df], axis=1)

    # loop
    for i in range (0, num): 
        if float(df.loc[i, "pitch_number"]) == 2: # when the pitch number is 2
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
        elif float(df["pitch_number"][i]) == 3: # when the pitch number is 3
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
            df.at[i, "pre2"] = df.loc[i + 2, "pitch_type"]
        elif float(df["pitch_number"][i]) > 3: # when the pitch number is bigger than 3
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
            df.at[i, "pre2"] = df.loc[i + 2, "pitch_type"]
            df.at[i, "pre3"] = df.loc[i + 3, "pitch_type"]

    # one-hot encoding for 'stand' as it is categorical data
    stand_df = pd.get_dummies(df.stand, prefix='stand')
    df.drop(["stand"], axis=1, inplace=True)
    df = pd.concat([df, stand_df], axis=1)

    df = df.dropna()

    df.head(40)



    # Just used RandomizedSearchCV() instead of butre forcing various hyperparameter combinations

    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import GradientBoostingClassifier
    from scipy.stats import uniform as sp_randFloat
    from scipy.stats import randint as sp_randInt
    from sklearn.model_selection import RandomizedSearchCV

    model = GradientBoostingClassifier(random_state=1)

    X=df[['balls', 'strikes','on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', 'pitch_number', 'score_difference', 'pre1', 'pre2', 'pre3','stand_L', 'stand_R']]  # Features
    y=df['pitch_type']  # Labels
    y=y.astype('float')
            

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    parameters = {"subsample": sp_randFloat(),
                "n_estimators": sp_randInt(100, 800),
                "max_depth": sp_randInt(3, 10),
                "learning_rate": sp_randFloat()
                }

    best_model = RandomizedSearchCV(estimator=model, param_distributions=parameters, scoring='accuracy',
                            cv=5, n_iter=100, n_jobs=-1)
    best_model.fit(X_train, y_train)

    print("Results from Random Search ")
    print(" The best estimator across ALL searched params:", best_model.best_estimator_)
    print("\n   The best score across ALL searched params:", best_model.best_score_)
    print("\n   The best parameters across ALL searched params:", best_model.best_params_)

    if len(ptm_list) == 2:
        score_list_2.append(best_model.best_score_)
    elif len(ptm_list) == 3:
            score_list_3.append(best_model.best_score_)
    elif len(ptm_list) == 4:
            score_list_4.append(best_model.best_score_)
    elif len(ptm_list) == 5:
            score_list_5.append(best_model.best_score_)
    elif len(ptm_list) == 6:
            score_list_6.append(best_model.best_score_)
    elif len(ptm_list) == 7:
            score_list_7.append(best_model.best_score_)
    elif len(ptm_list) == 8:
            score_list_8.append(best_model.best_score_)
    
    
    # See the best model's confusion matrix and precision score

    # from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score
    # import matplotlib.pyplot as plt

    # # best_model.classes_
    # predictions = best_model.predict(X_train)
    # cm = confusion_matrix(y_train, predictions, labels=best_model.classes_)
    # disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=ptm_list)
    # disp.plot()

    # plt.show()

    # p = precision_score(y_train, predictions, average='micro')
    # print("Precision Score=", p)

    # save the model
    import joblib

    joblib.dump(best_model, f'{int(player_id)}.pkl')
    
    print("\nPlayer id " + str(player_id) + ", " + str(player_name) + "'s training now has done\n")

    



if len(score_list_2) != 0:
    print(score_list_2)

    result_2 = 0
    for val in score_list_2:
        result_2 += val  
   
    print(f"score_list_2 average : {result_2 / len(score_list_2)}")


##############################################


if len(score_list_3) != 0:
    print(score_list_3)

    result_3 = 0
    for val in score_list_3:
        result_3 += val  
    
    print(f"score_list_3 average : {result_3 / len(score_list_3)}")


##############################################


if len(score_list_4) != 0:
    print(score_list_4)

    result_4 = 0
    for val in score_list_4:
        result_4 += val 
    
    print(f"score_list_4 average : {result_4 / len(score_list_4)}")


##############################################


if len(score_list_5) != 0:
    print(score_list_5)

    result_5 = 0
    for val in score_list_5:
        result_5 += val  
    
    print(f"score_list_5 average : {result_5 / len(score_list_5)}")


##############################################


if len(score_list_6) != 0:
    print(score_list_6)

    result_6 = 0
    for val in score_list_6:
        result_6 += val  

    print(f"score_list_6 average : {result_6 / len(score_list_6)}")


##############################################


if len(score_list_7) != 0:
    print(score_list_7)

    result_7 = 0
    for val in score_list_7:
        result_7 += val 
 
    print(f"score_list_7 average : {result_7 / len(score_list_7)}")


##############################################


if len(score_list_8) != 0:
    print(score_list_8)

    result_8 = 0
    for val in score_list_8:
        result_8 += val  

    print(f"score_list_8 average : {result_8 / len(score_list_8)}")

