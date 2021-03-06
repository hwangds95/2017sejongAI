from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

# Define input text
input_text = "That's what this presidency has tried to be about.  And I see that in the young people I've worked with.  I couldn't be prouder of them.  And so this is not just a matter of No Drama Obama -- this is what I really believe.  It is true that behind closed doors I curse more than I do publicly.  And sometimes I get mad and frustrated, like everybody else does.   But at my core, I think we're going to be okay.  We just have to fight for it.  We have to work for it, and not take it for granted.  And I know that you will help us do that."

# Sentence tokenizer 
print("\nSentence tokenizer:")
print(sent_tokenize(input_text))

# Word tokenizer
print("\nWord tokenizer:")
print(word_tokenize(input_text))

# WordPunct tokenizer
print("\nWord punct tokenizer:")
print(WordPunctTokenizer().tokenize(input_text))
