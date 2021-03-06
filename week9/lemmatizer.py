from nltk.stem import WordNetLemmatizer

input_words = ['i', 'am', 'boy', 'girl', 'I', 'like', 
        'ice cream', 'swim', 'dance', 'holiday', 'Christmas', 'candy']

# Create lemmatizer object 
lemmatizer = WordNetLemmatizer()

# Create a list of lemmatizer names for display
lemmatizer_names = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
formatted_text = '{:>24}' * (len(lemmatizer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *lemmatizer_names), 
        '\n', '='*75)

# Lemmatize each word and display the output
for word in input_words:
    output = [word, lemmatizer.lemmatize(word, pos='n'),
           lemmatizer.lemmatize(word, pos='v')]
    print(formatted_text.format(*output))
