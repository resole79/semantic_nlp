import spacy  

nlp = spacy.load('en_core_web_md')
# nlp = spacy.load('en_core_web_sm')


def word_similarity(list_of_word):
    for i, word in enumerate(list_of_word):
        word_nlp = nlp(word)
        for word_1 in list_of_word:
            word_nlp_1 = nlp(word_1)
            if word != word_1:
                print(f"{word_nlp} similarity with {word_nlp_1} : {word_nlp.similarity(word_nlp_1)}")

        list_of_word.pop(0)
        if len(list_of_word) > 1:
            word_similarity(list_of_word)


print("\n-- PDF example --")
# PDF example
words_list = ["cat", "monkey", "banana"]
word_similarity(words_list)

# cat similarity with monkey - they are both animals and the chance of similarity are highest
# cat similarity with banana - they are very little correlation, lowest similarity level of all three
# monkey similarity with banana - spacy maybe knows that monkeys like the banana and for this shown a correlation

print("\n-- My own example --")
# My own example
words_list_1 = ["king", "sun", "singer"]
word_similarity(words_list_1)

# king similarity with sun - maybe spacy knows King Sun was a King of France since 1643 till 1715
# king similarity with singer - the singer is a king if you think about Freddy Mercury ^_^
# sun similarity with singer - they don't have correlation


# When I use the small model "en_core_web_sm" occurrent an error  of "UserWarning", this because no word vectors loaded,
# so the result not give useful similarity judgements.
# When we had run  the file "example.py", also we can note :
# if we use "en_core_web_sm" the result of similarity complains is lowest respect when we use "en_core_web_mb",
# because the model is smaller respect the other.
