from __future__ import print_function
import sklearn as sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import precision_score, recall_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from classificationMethod import classificationMethod
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from nltk.stem.snowball import SnowballStemmer


# This class is used to apply My BEst Configuration for all 4 classification methods (NB, LR, SVM, RF)
class MBC_Comparison:
    def __init__(self, training_set, evaluation_set):
        self.training_set = training_set
        self.evaluation_set = evaluation_set
        self.nb = classificationMethod("NB", 0, 0, 0, "MBC_NB")
        self.lr = classificationMethod("LR", 0, 0, 0, "MBC_LR")
        self.svm = classificationMethod("SVM", 0, 0, 0, "MBC_SVM")
        self.rf = classificationMethod("RF", 0, 0, 0, "MBC_RF")
        self.myMethods = [self.nb, self.lr, self.svm, self.rf]

    # This method calls all 4 classification methods with My Best Configuration
    def apply_mbc(self):
        self.naive_bayes_MBC()
        self.logistic_regression_MBC()
        self.svm_MBC()
        self.random_forests_MBC()

    # This function is used to calculate and set the precision score, recall score
    # and f1 sore of the provided classification method
    def populateScores(self, classificationMethod, predicted_set):
        # Calculate Macro-Precision Score
        precision_score_unigram = precision_score(self.evaluation_set.target,
                                                  predicted_set,
                                                  average='macro')
        classificationMethod.setPrecision(precision_score_unigram)

        # Calculate Recall Score
        recall_score_unigram = recall_score(self.evaluation_set.target,
                                            predicted_set,
                                            average='macro')
        classificationMethod.setRecall(recall_score_unigram)

        # Calculate F1 Score
        f1_score_unigram = sklearn.metrics.f1_score(self.evaluation_set.target,
                                                    predicted_set,
                                                    average='macro')
        classificationMethod.setF1(f1_score_unigram)

    # This function is used during the stemming process
    def stemmed_words(doc, stemmer, analyzer):
        return lambda doc: (stemmer.stem(w) for w in analyzer(doc))

    # This function represents my best configuration for naive bayes.
    # It applies stemming, ignore stop words, lower case words by default, uses count vectorizer
    # For hyperparameters, it uses alpha = 0.01
    def naive_bayes_MBC(self):
        stemmer = SnowballStemmer("english")
        analyzer = CountVectorizer().build_analyzer()
        count_vect = CountVectorizer(encoding='latin-1', stop_words='english',
                                     analyzer=self.stemmed_words(stemmer, analyzer))
        X_train_counts = count_vect.fit_transform(self.training_set.data)
        clf = MultinomialNB(alpha=.01).fit(X_train_counts, self.training_set.target)
        X_new_counts = count_vect.transform(self.evaluation_set.data)
        predicted = clf.predict(X_new_counts)
        self.populateScores(self.nb, predicted)

    # This function represents my best configuration for logistic regression.
    # It applies stemming, ignore stop words, lower case words by default, uses count vectorizer
    # It also uses select from model as feature selection. When it comes to hyperparameters, it has maximum
    # number of iterations defined
    def logistic_regression_MBC(self):
        stemmer = SnowballStemmer("english")
        analyzer = CountVectorizer().build_analyzer()
        my_pipe = Pipeline([('vect', CountVectorizer(encoding='latin-1', stop_words='english',
                                                     analyzer=self.stemmed_words(stemmer, analyzer))),
                            ('feature_selection', SelectFromModel(LogisticRegression(max_iter=10000))),
                            ('classification', LogisticRegression(max_iter=10000))])
        my_pipe.fit(self.training_set.data, self.training_set.target)
        predicted = my_pipe.predict(self.evaluation_set.data)
        self.populateScores(self.lr, predicted)

    # This function represents my best configuration for SVM.
    # It applies stemming, ignores stop words, lower cases words by default, and uses tfidf,
    # It also uses select from model feature selection. When it comes to hyperparameters, it has maximum
    # number of iterations defined
    def svm_MBC(self):
        stemmer = SnowballStemmer("english")
        analyzer = CountVectorizer().build_analyzer()
        my_pipe = Pipeline([('vect', CountVectorizer(encoding='latin-1', stop_words='english',
                                                     analyzer=self.stemmed_words(stemmer, analyzer))),
                            ('tfidf', TfidfTransformer()),
                            ('feature_selection', SelectFromModel(svm.LinearSVC(max_iter=10000))),
                            ('classification', svm.LinearSVC(max_iter=10000))])
        my_pipe.fit(self.training_set.data, self.training_set.target)
        predicted = my_pipe.predict(self.evaluation_set.data)
        self.populateScores(self.svm, predicted)

    # This function represents my best configuration for Random forests
    # It applies stemming, ignores stop words, lower cases words by default, and uses tfidf
    # It also uses select from model feature selection. When it comes to hyperparameters, it
    # has random state as 0
    def random_forests_MBC(self):
        stemmer = SnowballStemmer("english")
        analyzer = CountVectorizer().build_analyzer()
        my_pipe = Pipeline([('vect', CountVectorizer(encoding='latin-1', stop_words='english',
                                                     analyzer=self.stemmed_words(stemmer, analyzer))),
                            ('tfidf', TfidfTransformer()),
                            ('feature_selection', SelectFromModel(RandomForestClassifier(random_state=0))),
                            ('classification', RandomForestClassifier(random_state=0))])
        my_pipe.fit(self.training_set.data, self.training_set.target)
        predicted = my_pipe.predict(self.evaluation_set.data)
        self.populateScores(self.rf, predicted)
