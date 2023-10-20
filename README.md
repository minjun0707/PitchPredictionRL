
<p align="center"><img width="570" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/609e82cd-4770-424d-b15a-782def482fb1"></p>

<div align='center'>
  <h1>⚾ Pitch Prediction</h1>

<a href="www.google.com">Presentation Video on Youtube</a><br><br>
<a href="https://pitchingbaseball.duckdns.org">Our Website</a>

<p>
<p>


</div>



# Overview


## Brief description  
Hall of Fame outfielder and former Home Run King Hank Aaron once said:  
"_**Guessing what the pitcher is going to throw is 80% of being a successful hitter**_. The other 20% is just execution."  
  
This project aims to help batter's batting when they are in the plate by predicting the pitcher's next pitch through predicting the next pitch via a machine learning model and action recommendation via reinforcement learning.  
  
## Objective
The objective of this project is simple: Helping batters to improve their batting via predicting the next picth.

To accomplish this objective,  
1. We built machine learning models of every active MLB pitcher that predict the next pitch type of the pitcher.  
2. Based on the predicted result, we recommend the action that a batter should do via reinforce learning model.
3. Lastly, we provide a random video of the predicted pitch type that the pitcher throws.




## Expected effect
![image](https://github.com/001021/PitchPredictionRL/assets/94168462/55149946-4700-454d-9054-a95b0a5eaa63)

As we can see on the above graph, with the pitchers' evolution and the nature of the game (_even an MVP-level hitter can record a batting average of around .300, which means no matter how good the batter is, the pitcher wins 70% of the times_), batting average is constantly decreasing over the whole league.

We expect to batters improve their batting through our predictions and action recommendations.
# Key features


    Pitch prediction, Action recommendation, Video check

## Pitch prediction
* **Data used**    
    The MLB provides tons of pitch data freely.  
  
    We load those data through pybaseball library to do data analysis and predict the next pitch type through these data.  
  
![image](https://github.com/001021/PitchPredictionRL/assets/94168462/ba35016c-294a-44ef-adcf-2d73b92b3d6e)

* **Classifier Selection**  
    We tried 3 different classifiers – Gradient Boosting, Random Forest, Naïve Bayes Classifier.
    
    Above 3 classifiers mentioned, Gradient Boosting gives the best performance.  
  
    Gradient Boosting gives the best accuracy generally among the pitchers we’ve tested, especially when it comes to predict breaking balls (which has relatively small portion of a pitcher’s arsenal).  
  
    Tyler glasnow's confusion matrix (In order of gradient bossting, random forest, naïve bayes)
    
![image](https://github.com/001021/PitchPredictionRL/assets/94168462/88c9650e-6ebf-4d2b-8e2d-0aea26f27ced)

* **Feature selection**  
    First, we selected 10 features that are considered to be relative with pitch type in baseball common-sense and created 4 features.  
    _'balls', 'strikes','on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', 'pitch_number', 'score_difference', 'pre1', 'pre2', 'pre3', 'stand_L', 'stand_R'_  
  
    But we couldn’t find any significant correlation with pitch type through a correlation matrix.  
  
    Then, we tried Chi-Squared Test for feature selection.  
  
    It both selected only ‘balls’, ‘strikes’, ‘pre1’ --> but this only has led to lower performance of the models.  
  
![image](https://github.com/001021/PitchPredictionRL/assets/94168462/e1c715ae-c082-4d6b-99ac-96a8085aedd2)  
   
    After that, we only have chosen features that have p-value lower than 0.05 through Pearson’s correlation.  
  
    It still shows lower performance than the first one, but at least it showed better accuracy on most pitched pitch type. 
  
![image](https://github.com/001021/PitchPredictionRL/assets/94168462/c1cce3f8-0882-4fd0-a0e0-f0fe20629ba8)  
  
    But in most cases, models with the features that we’ve selected at first showed better performance overall.  
  
    So we trained the models for each pitchers with the features that we’ve selected at first.  

* **Model save & load**   
    After we trained each model for each pitchers, we saved the model with the player id at the server using Joblib library.    
  
    https://joblib.readthedocs.io/en/stable/  

## Reinforcement learning

* **Q-Learning**

    Q-Learning is a form of reinforcement learning that enables an agent (in this case, the batter) to make optimal decisions in a given environment (the baseball game) by learning from experience.

**Training with Q-Learning Model**

    To train the Q-Learning model, the pitch prediction results are used as input.
The pitch type predicted by the pitch prediction algorithm serves as the current state, and the available actions are categorized into three options: swing at the pitch, attempt a cutting hit, or intentionally foul the ball.
The model is trained using a reward system that evaluates the outcomes of these actions, considering factors such as successful hits, strikes, and outs.

<br>
<div align="center">
<b>State / Action / Reward</b>
</div>

<img src="https://github.com/001021/PitchPredictionRL/assets/84309420/c34a1733-e658-4385-ad55-8b84a3fcec6b" width="300" height="300"/>&nbsp;&nbsp;&nbsp;<img src="https://github.com/001021/PitchPredictionRL/assets/84309420/c46e049d-c648-4343-b840-982dd9ea6b4e" width="400" height="300" />


    During the training process, the Q-Learning model updates the Q-values in the Q-table based on the rewards obtained from each action.
    By repeatedly playing simulated at-bats and refining the Q-values, the model gradually learns the optimal actions to take for each predicted pitch type.
![training](https://github.com/001021/PitchPredictionRL/assets/84309420/5b06b98c-e638-4f5a-ad92-29a9acb83272)


**Action Recommendation Process**

    Once the Q-Learning model has been trained, it can be used to make real-time action recommendations for batters. When a new pitch type is predicted, the model refers to the Q-table to determine the recommended action with the highest expected reward.

![result](https://github.com/001021/PitchPredictionRL/assets/84309420/e2acaed3-baa9-4587-b7bc-ea01510300a7)




## Providing a random video of the precited pitch type    
* **At the result**    
    You can get the predicted pitch type, an action recommendation and also **a random video of the predicted pitch tpye**.  
  
    
<img width="388" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/f7ec610c-b2bd-4720-88e0-451ec134ba32">

# System structure

<img width="1025" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/f9b4e243-7dbe-4d60-bcc2-a6069fc85974">
<br><br>


- [Frontend Server]  
    * The frontend server uses the React framework
    * Receives 12 game situation parameters from the user and sends them to the backend server
- [Backend Server]  
    * The backend server uses the Spring framework.
    * Proceed with verification of the value received from the front-end server
    * The backend server performs preprocessing on the received input values and sends them to the data processing server

- [Data Processing Server]  
    * Reinforcement learning, pitch prediction, and pitch tipping prediction are performed through the values ​​received from the backend server.

# API

- Predict next pithc type API basic information. 

API that receives the predicted next pitch type, probability, and batter behavior recommendation as a result value
when sending a request by entering the game situation, 
<br>

|Method|URL|
|-|-|
|POST|https://pitchingbaseball.duckdns.org/api/pitch-detection|

<br>

- request
<br>


|Name|Type|Description|Required variable|
|-|-|-|-|
|name|String|pitcher name|o|
|score_difference|String|The score difference between the two teams|o|
|on_1b|Boolean|Whether there is a runner on first base|o|
|on_2b|Boolean|Whether there is a runner on second base|o|
|on_3b|Boolean|Whether there is a runner on third base|o|
|inning|String|current inning|o|
|stand|String|batter position|o|
|strikes|String|strike count|o|
|balls|String|ball count|o|
|pitch_number|String|The number of pitches thrown by the pitcher|o|
|pre1|String|The pitch type thrown in the previous pitch|o|
|pre2|String|The pitch type thrown in the second previous pitch|o|
|pre3|String|The pitch type thrown in the third previous pitch|o|

<br>

- Response

<br>

|Name|Type|Description|
|-|-|-|-
|pitchType|String|The predicted pitch type that the pitcher is expected to throw next|
|probability|String|Predictability|
|action|String|Recommendation for the action the batter should perform|


<br>


- Example


<br>


	curl -X POST -H "Content-Type: application/json" -d
    '{
         "name": "Tyler glasnow", 
         "score_difference": "7",
         "on_1b": true,
         "on_2b": false, 
         "on_3b": true,
         "inning" : "7",
         "stand": "left", 
         "strikes": "2",
         "balls" : "1",
         "pitch_number": "23", 
         "pre1": "1",
         "pre2" : "3",
         "pre3" : "2"
    }'

<br>

    HTTP/1.1  200 OK Content-Type: application/json;charset=UTF-8  
    {  
	    "pitchType":"fastball", 
	    "probability":"0.777",
	    "action": "hit"
    }



# User Interface
 - **Web**
<br>
<img width="800" height="700" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/e4ccca4c-ef10-4e7f-a29d-0743d4c0ceaf">
<br>
<br>
<br>
<br>

 - **User Input**
> User needs to input the following baseball game situation:  
> Pitcher name, Strike count, Ball count, Base situation, Out count, Inning, Pitch count, Score difference, Last three pitches thrown
<br>
<img width="285" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/fcb2c727-6379-40af-8791-69c6e0ef6722">
<br>
<br>
<br>
<br>


 - **Click Predict Button**
> Enter all the variable values regarding the game situation and click the pitch prediction button
<br>
<img width="201" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/40b4bdd1-fe69-4004-8e75-3279fb5e2759"> 
<br>

<br>
<br>
<br>


 - **Result**
> The user can see three possible outcomes:  
> pitcher's next pitch prediction, recommended actions for the batter, and pitching motion analysis
<br>
<img width="482" alt="image" src="https://github.com/001021/PitchPredictionRL/assets/75360915/220493f2-9bd5-4e17-8707-a193ca915c39">
<br>

<br>
<br>
<br>

---




# Used library

### For the classification models
* **pybaseball**    
Used for collecting pitchers' data  
https://github.com/jldbc/pybaseball  

* **pandas**  
Used for data analysis  
https://pandas.pydata.org. 

* **scikit-learn**  
Used for model training  
https://scikit-learn.org/stable/  

* **Joblib**   
Used for model save & load  
https://joblib.readthedocs.io/en/stable/

### For the Reinforcement Learning
* **random**  
Used for choice random action  
https://docs.python.org/3/library/random.html

* **gym**  
Used for build RL environments  
https://gym.openai.com/docs/

* **predictMain**  
Used for receive pitch prediction

  
# Member Informaiton

김민준 - Web Server  
박준영 - Data Analysis  
윤주은 - Reinforcement Learning
