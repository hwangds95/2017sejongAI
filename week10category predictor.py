
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

category_map = {'talk.politics.misc': 'Politics', 'rec.autos': 'Autos',
 'rec.sport.hockey': 'Hockey', 'sci.electronics': 'Electronics',
 'sci.med': 'Medicine'}

training_data = fetch_20newsgroups(subset='train',
 categories=category_map.keys(), shuffle=True, random_state=5)

count_vectorizer = CountVectorizer()
train_tc = count_vectorizer.fit_transform(training_data.data)
print("\nDimensions of training data:", train_tc.shape)

tfidf = TfidfTransformer()
train_tfidf = tfidf.fit_transform(train_tc)

input_data = [
 'Under the Red, White, and Blue',
 'Then wear the gold hat, if that will move her;',
 'If you can bounce high, bounce for her too,',
 'Till she cry "Lover, gold-hatted, high-bouncing lover,'
]

classifier = MultinomialNB().fit(train_tfidf, training_data.target)

input_tc = count_vectorizer.transform(input_data)

3/6
input_tfidf = tfidf.transform(input_tc)

predictions = classifier.predict(input_tfidf)

for sent, category in zip(input_data, predictions):
 print('\nInput:', sent, '\nPredicted category:', \
 category_map[training_data.target_names[category]])
