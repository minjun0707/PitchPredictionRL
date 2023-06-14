from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from scipy.stats import uniform as sp_randFloat
from scipy.stats import randint as sp_randInt


def dataProcessor(df) :
    model = GradientBoostingClassifier(random_state=1)

    X = df[['balls', 'strikes', 'on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', 'pitch_number', 'score_difference',
            'pre1', 'pre2', 'pre3', 'stand_L', 'stand_R']]  # Features
    y = df['pitch_type']  # Labels
    y = y.astype('float')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    parameters = {"subsample": sp_randFloat(),
                  "n_estimators": sp_randInt(100, 800),
                  "max_depth": sp_randInt(1, 8)
                  }

    best_model = RandomizedSearchCV(estimator=model, param_distributions=parameters,
                                    cv=3, n_iter=10, n_jobs=-1)
    best_model.fit(X_train, y_train)

    print("Results from Random Search ")
    print(" The best estimator across ALL searched params:", best_model.best_estimator_)
    print("\n   The best score across ALL searched params:", best_model.best_score_)
    print("\n   The best parameters across ALL searched params:", best_model.best_params_)

    return best_model