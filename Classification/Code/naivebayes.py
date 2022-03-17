from functions import *

dataset = load_dataset("/Users/connormcdonald/Desktop/Masters/MIT807/Data/twitter_training.csv", ['target', 't_id', 'created_at', 'query', 'user', 'text'])
print('dataset loaded')

n_dataset = remove_unwanted_cols(dataset, ['t_id', 'created_at', 'query', 'user'])
dataset.text = dataset['text'].apply(preprocess_tweet_text)
print('dataset processed')

# Same tf vector will be used for Testing sentiments on unseen trending data
tf_vector = get_feature_vector(np.array(dataset.iloc[:, 1]).ravel())
X = tf_vector.transform(np.array(dataset.iloc[:, 1]).ravel())
y = np.array(dataset.iloc[:, 0]).ravel()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)
print('train test split complete')

# Training Naive Bayes model
NB_model = MultinomialNB()
print('model training')
NB_model.fit(X_train, y_train)

print('model validating')
y_predict_nb = NB_model.predict(X_test)
print(accuracy_score(y_test, y_predict_nb))