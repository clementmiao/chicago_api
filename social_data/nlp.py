from social_data.models import Post, Service, Sentiment
import nltk
from os import path
import pickle

def get_list(file_name):
    BASE_DIR = path.dirname(__file__)
    rel_path = file_name
    file_path = path.join(BASE_DIR, rel_path)
    f = open(file_path)
    lines = f.read().splitlines()
    f.close()
    return lines

def format_string(list):
    return_list = []
    for element in list:
        l = element.split('\t')
        string = l[0]
        value = float(l[1])
        sent = ''
        if value >= 0:
            sent = 'positive'
        else:
            sent = 'negative'
        return_list.append((string, sent))
    return return_list

def format_string_2(list):
    return_list = []
    for element in list:
        l = element.split('\t')
        string = l[0]
        sent = l[1]
        return_list.append((string, sent))
    return return_list

def format_string_kaggle(list):
    return_list = []
    for element in list:
        l = element.split('\t')
        value = float(l[0])
        string = l[1]
        sent = ''
        if value == 1:
            sent = 'positive'
        else:
            sent = 'negative'
        return_list.append((string, sent))
    return return_list





def process():
    lines_1 = get_list('twitter_data/unigrams-pmilexicon.txt')
    lines_2 = get_list('twitter_data/bigrams-pmilexicon.txt')
    lines_3 = get_list('twitter_data/bigrams-pmilexicon_2.txt')
    lines_4 = get_list('twitter_data/sentimenthashtags.txt')
    lines_5 = get_list('twitter_data/unigrams-pmilexicon_2.txt')
    lines_6 = get_list('twitter_data/kaggle_data.txt')
    # lines = lines_1 + lines_2 + lines_3 + lines_5
    lines = lines_6

    lines_4 = format_string_2(lines_4)

    # rv = format_string(lines) + lines_4
    rv = format_string_kaggle(lines)
    pos_tweets = []
    neg_tweets = []

    for element in rv:
        if element[1] == 'positive':
            pos_tweets.append(element)
        else:
            neg_tweets.append(element)

    tweets = []

    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split()]
        tweets.append((words_filtered, sentiment))

    def get_words_in_tweets(tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_word_features(wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features

    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features
    print "tweets created"
    word_features = get_word_features(get_words_in_tweets(tweets))
    print "word features"
    training_set = nltk.classify.apply_features(extract_features, tweets)
    print "training set"
    classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
    print "classifier"
    return (classifier, word_features)


def save_classifier(tuple):
    BASE_DIR = path.dirname(__file__)
    rel_path = 'my_classifier.pickle'
    file_path = path.join(BASE_DIR, rel_path)
    f = open(file_path, 'wb')
    pickle.dump(tuple, f)
    f.close()


def word_feats(words):
    return dict([(word, True) for word in words])

def getwords(tweets):
    allwords = []
    for (words, sentiment) in tweets:
        allwords.extend(words)
    return allwords

def getwordfeatures(listoftweets):
    #Print out wordfreq if you want to have a look at the individual counts of words.
    wordfreq = nltk.FreqDist(listoftweets)
    words = wordfreq.keys()
    return words

def intermediary():
    movie_reviews = nltk.corpus.movie_reviews
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')

    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
    lines_1 = get_list('twitter_data/unigrams-pmilexicon.txt')
    lines_2 = get_list('twitter_data/bigrams-pmilexicon.txt')
    lines_3 = get_list('twitter_data/bigrams-pmilexicon_2.txt')
    lines_4 = get_list('twitter_data/sentimenthashtags.txt')
    lines_5 = get_list('twitter_data/unigrams-pmilexicon_2.txt')

    lines = lines_1 + lines_2 + lines_3 + lines_5

    lines = lines_2 + lines_3

    lines_6 = get_list('twitter_data/kaggle_data.txt')

    kaggle = format_string_kaggle(lines_6)

    lines_4 = format_string_2(lines_4)

    # rv = format_string(lines)
    
    rv = format_string(lines_2)
    # rv = kaggle

    length = len(rv)

    cutoff = length * 1/100

    rv = rv[:cutoff]

    # rv = rv + kaggle

    pos_tweets = []
    neg_tweets = []

    for element in rv:
        if element[1] == 'positive':
            pos_tweets.append(element)
        else:
            neg_tweets.append(element)

    tweets = []

    for (words, sentiment) in pos_tweets + neg_tweets:
        words_filtered = [e.lower() for e in words.split()]
        tweets.append((words_filtered, sentiment))

    return tweets

def get_corpus():
    
    tweets = intermediary()

    
 
    # trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    # testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    # trainfeats = negfeats + posfeats
    

    


    # print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
    # classifier.show_most_informative_features(1000)

    wordlist = getwordfeatures(getwords(tweets))
    wordlist = [i for i in wordlist if not i in nltk.corpus.stopwords.words('english')]

    def feature_extractor(doc):
        docwords = set(doc)
        features = {}
        for i in wordlist:
            features['contains(%s)' % i] = (i in docwords)
        return features

    training_set = nltk.classify.apply_features(feature_extractor, tweets)
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    return (classifier, wordlist)

def testing():
    tweets = intermediary()
    wordlist = getwordfeatures(getwords(tweets))
    wordlist = [i for i in wordlist if not i in nltk.corpus.stopwords.words('english')]

    def feature_extractor(doc):
        docwords = set(doc)
        features = {}
        for i in wordlist:
            features['contains(%s)' % i] = (i in docwords)
        return features

    training_set = nltk.classify.apply_features(feature_extractor, tweets)
    BASE_DIR = path.dirname(__file__)
    rel_path = 'my_classifier.pickle'
    file_path = path.join(BASE_DIR, rel_path)
    f = open(file_path)
    tup = pickle.load(f)
    f.close()
    classifier = tup[0]
    print nltk.classify.accuracy(classifier, training_set)



def extract_features(document, wordlist):

        document_words = set(document)

        features = {}

        for word in wordlist:

            features['contains(%s)' % word] = (word in document_words)

        return features

def assess_tweet(input, classifier, wordlist):
    input = input.lower().split()

    return classifier.classify(extract_features(input, wordlist))

def save_current():
    tup = get_corpus()
    save_classifier(tup)

def process_tweets():
    s = Service.objects.get(name="twitter")
    tweets_list = Post.objects.filter(service=s)
    tup = get_corpus()
    classifier = tup[0]
    wordlist = tup[1]
    # classifier = process()
    for x in tweets_list:
        result = assess_tweet(x.text, classifier, wordlist)
        if result != 'positive':
            print x.text
            print result
        # senti = Sentiment(post = x, sentiment = result)
        # senti.save()    
