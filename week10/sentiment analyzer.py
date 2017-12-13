from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy 

def extract_features(words):
  return dict([(word, True) for word in words]) 

if __name__=='__main__':
  fileids_pos = movie_reviews.fileids('pos')
  fileids_neg = movie_reviews.fileids('neg')
  features_pos = [(extract_features(movie_reviews.words(fileids=[f])), 'Positive') for f in fileids_pos]
  features_neg = [(extract_features(movie_reviews.words(fileids=[f])), 'Negative') for f in fileids_neg]
  threshold = 0.8
  num_pos = int(threshold * len(features_pos))
  num_neg = int(threshold * len(features_neg))
  features_train = features_pos[:num_pos] + features_neg[:num_neg]
  features_test = features_pos[num_pos:] + features_neg[num_neg:]   
  classifier = NaiveBayesClassifier.train(features_train)
  print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test))
  
  N = 15
  print('\nTop ' + str(N) + ' most informative words:')
  for i, item in enumerate(classifier.most_informative_features()):
    print(str(i+1) + '. ' + item[0])
    if i == N - 1:
      break
  input_reviews = [
    'Every single characterization was a bit off and some of them felt like they were forced, especially Barry Allen. Still, the actors do the best they can with the material so it is not unbearable. ',
    'Every One Star or Ten Star is a lie, it is a good movie, not terrible, not amazing, good.',
    'It is a very funny movie with good characters that we love.',
    'Entertaining, OK... but how confusing!!']
  print("\nMovie review predictions:")
  for review in input_reviews:
    print("\nReview:", review) 
    probabilities = classifier.prob_classify(extract_features(review.split())) 
    predicted_sentiment = probabilities.max() 
    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2)) 
