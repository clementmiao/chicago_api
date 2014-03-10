from social_data.models import Post, Service, Sentiment
import nltk

def word_feats(words):
    return dict([(word, True) for word in words])

def feature_extractor(doc):
    wordlist = []
    wordlist = [i for i in wordlist if not i in nltk.corpus.stopwords.words('english')] 
    docwords = set(doc)
    features = {}
    for i in wordlist:
        features['contains(%s)' % i] = (i in docwords)
    return features

def extract_features(document):

    document_words = set(document)

    features = {}

    wordlist = []
    wordlist = [i for i in wordlist if not i in nltk.corpus.stopwords.words('english')] 

    for word in wordlist:

        features['contains(%s)' % word] = (word in document_words)

    return features


def get_corpus():
    movie_reviews = nltk.corpus.movie_reviews
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')

    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
 
    # trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    # testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    trainfeats = negfeats + posfeats
    # print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
    classifier = nltk.classify.NaiveBayesClassifier.train(trainfeats)
    # print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
    classifier.show_most_informative_features()
    return classifier

def assess_tweet(input, classifier):
    input = input.lower().split()

    return classifier.classify(extract_features(input))

def process_tweets():
    s = Service.objects.get(name="twitter")
    tweets_list = Post.objects.filter(service=s)
    classifier = get_corpus()
    for x in tweets_list:
        result = assess_tweet(x.text, classifier)
        if result != 'pos':
            print x.text
            print result
        # senti = Sentiment(post = x, sentiment = result)
        # senti.save()    
