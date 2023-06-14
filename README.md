# PitchPredictionRL
PitchPredictionRL is a project that focuses on predicting the primary pitch types a pitcher tends to throw in an ongoing baseball game. It takes into account the current game situation and pitch tipping cues to make accurate predictions. Using reinforcement learning techniques, it also provides recommendations on the optimal actions a batter should take to maximize rewards when facing a particular pitch type.

## Features
* Pitch type prediction: Based on the available game data and pitch tipping cues, the project predicts the most likely pitch type that a pitcher will throw in the current situation.

* Reinforcement learning: The project employs reinforcement learning algorithms to learn and recommend the best actions for a batter when a specific pitch type is thrown.

* Reward optimization: By considering various factors such as pitch velocity, movement, and batter's performance, the project aims to guide the batter towards actions that yield the highest rewards.

## Installation
1. Clone the repository:
```
git clone https://github.com/001021/PitchPredictionRL.git
```

2. Set up the virtual environment (optional but recommended):
```
cd PitchPredictionRL
python -m venv env
source env/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Prepare the necessary data: Ensure that you have the relevant game data and pitch tipping cues available for the prediction process.

2. Train the model: Run the training script to train the reinforcement learning model and optimize the reward predictions.

```
python train.py
```

3. Make predictions: Use the trained model to make pitch type predictions based on the current game situation and pitch tipping cues.  
(* You can get the models trained by us from this Google Drive link.)
```
python predict.py
```
4. Evaluate the performance: Assess the accuracy and effectiveness of the pitch type predictions and the recommended actions for batters.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
