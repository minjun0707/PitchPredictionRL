from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

def dataPreprocessing() :
    last_name = ''
    first_name = ''
    # info_table = playerid_lookup(last_name, first_name)

    info_table = playerid_lookup('Glasnow', 'Tyler')

    print(info_table)

    # get MLB player id value
    player_id = info_table.at[0, 'key_mlbam']

    # load pitch data
    df = statcast_pitcher('2017-03-01', '2019-09-30', player_id)

    # 원하는 column만 추출하기
    df = df[['pitch_type', 'stand', 'balls', 'strikes', 'on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning',
             'pitch_number', 'bat_score', 'fld_score']]

    # 주자 상황 적용하기
    for i in range(0, len(df["on_1b"].axes[0])):  # 1루 상황
        if df.loc[i, "on_1b"] > 0:  # 값이 있으면 1
            df.at[i, "on_1b"] = 1.0
        else:  # 없으면 0으로
            df.at[i, "on_1b"] = 0.0

    for i in range(0, len(df["on_2b"].axes[0])):  # 1루 상황
        if df.loc[i, "on_2b"] > 0:  # 값이 있으면 1
            df.at[i, "on_2b"] = 1.0
        else:  # 없으면 0으로
            df.at[i, "on_2b"] = 0.0

    for i in range(0, len(df["on_3b"].axes[0])):  # 1루 상황
        if df.loc[i, "on_3b"] > 0:  # 값이 있으면 1
            df.at[i, "on_3b"] = 1.0
        else:  # 없으면 0으로
            df.at[i, "on_3b"] = 0.0

    # drop rows with nan values
    df = df.dropna()

    # create new feature 'score_difference' and drop columns un-needed
    df["score_difference"] = df["fld_score"] - df["bat_score"]
    df.drop(["fld_score", "bat_score"], axis=1, inplace=True)

    print("score_difference 밑")
    print(len(df["pitch_type"].axes[0]))

    # get a pitch type of the pitcher
    pt_list = df['pitch_type'].unique()
    print(pt_list)

    # pitch arsenal percentage
    print(df['pitch_type'].value_counts(normalize=True) * 100)

    # drop pitch types that has been thrown less than 3%
    pt_filter = df.pitch_type.value_counts(normalize=True) > 0.03
    pt_index = pt_filter[pt_filter.values == True].index
    df = df[df.pitch_type.isin(list(pt_index))]

    # let's see how it has changed
    ptm_list = df['pitch_type'].unique()
    print(ptm_list)
    print(df['pitch_type'].value_counts(normalize=True) * 100)

    # mapping pitch_type with index of'pt_list'
    for i in range(0, len(ptm_list)):
        if i > len(ptm_list): break
        df['pitch_type'].mask(df['pitch_type'] == ptm_list[i], i + 1, inplace=True)

    # create temporary dataframe for previous pitch tendency dataframe
    pre_df = pd.DataFrame(0, index=np.arange(len(df["pitch_type"].axes[0])), columns=['pre1', 'pre2', 'pre3'])

    df = pd.concat([df, pre_df], axis=1)

    # loop
    for i in range(0, len(df["pitch_type"].axes[0])):
        if float(df.loc[i, "pitch_number"]) == 2:  # pitch number가 2일 때
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
        elif float(df["pitch_number"][i]) == 3:  # pitch number가 3일 때
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
            df.at[i, "pre2"] = df.loc[i + 2, "pitch_type"]
        elif float(df["pitch_number"][i]) > 3:  # pitch number가 3보다 클 때
            df.at[i, "pre1"] = df.loc[i + 1, "pitch_type"]
            df.at[i, "pre2"] = df.loc[i + 2, "pitch_type"]
            df.at[i, "pre3"] = df.loc[i + 3, "pitch_type"]

    # one-hot encoding for 'stand' as it is categorical data
    stand_df = pd.get_dummies(df.stand, prefix='stand')
    df.drop(["stand"], axis=1, inplace=True)
    df = pd.concat([df, stand_df], axis=1)

    df = df.dropna()
    return df,ptm_list
