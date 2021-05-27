import sklearn as sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from classificationMethod import classificationMethod
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import plotly.graph_objects as go
from sklearn import svm


# This class is used to apply the unigram and bigram of all 4 classification methods (NB, LR, SVM, RF) and
# to optionally display the learning curve
class BasicComparison:
    def __init__(self, training_set, evaluation_set):
        self.training_set = training_set
        self.evaluation_set = evaluation_set
        self.naive_unigram = classificationMethod("NB", 0, 0, 0, "UB")
        self.naive_bigram = classificationMethod("NB", 0, 0, 0, "BB")
        self.lr_unigram = classificationMethod("LR", 0, 0, 0, "UB")
        self.lr_bigram = classificationMethod("LR", 0, 0, 0, "BB")
        self.svm_unigram = classificationMethod("SVM", 0, 0, 0, "UB")
        self.svm_bigram = classificationMethod("SVM", 0, 0, 0, "BB")
        self.rf_unigram = classificationMethod("RF", 0, 0, 0, "UB")
        self.rf_bigram = classificationMethod("RF", 0, 0, 0, "BB")
        self.myMethods = [self.naive_unigram, self.naive_bigram,
                          self.lr_unigram, self.lr_bigram,
                          self.svm_unigram, self.svm_bigram,
                          self.rf_unigram, self.rf_bigram]

    # This method is used to train models using NB, LR, SVM, and RF methods with both unigram and bigram
    # baselines with a feature representation of Count Vectorization. It also tests the trained models
    # using the evaluation data, and calculates the macro precision, macro recall, and f1 scores
    # based on the models' predictions on the evaluation data
    def applyBasicComparison(self):
        # Compute feature representations(with both unigram and bigram) via Count Vectorizer using
        # the training and evaluation data
        UB_training_count, UB_evaluation_count = self.count_vectorizer(self.training_set.data,
                                                                       self.evaluation_set.data,
                                                                       n_gram=(1, 1))
        BB_training_count, BB_evaluation_count = self.count_vectorizer(self.training_set.data,
                                                                       self.evaluation_set.data,
                                                                       n_gram=(2, 2))
        # <---------- Naive Bayes Basic Unigram ---------->
        # train the model, test it using evaluation data
        nb_unigram_predicted = self.basic_naive_bayes(self.training_set.target,
                                                      UB_training_count,
                                                      UB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.naive_unigram, nb_unigram_predicted)
        # <---------- Naive Bayes Basic Bigram ---------->
        # train the model, test it using evaluation data
        nb_bigram_predicted = self.basic_naive_bayes(self.training_set.target,
                                                     BB_training_count,
                                                     BB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.naive_bigram, nb_bigram_predicted)
        # <---------- Logistic Regression Unigram ---------->
        # train the model, test it using evaluation data
        lr_unigram_predicted = self.basic_logistic_regression(self.training_set.target,
                                                              UB_training_count,
                                                              UB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.lr_unigram, lr_unigram_predicted)
        # <---------- Logistic Regression Bigram ---------->
        # train the model, test it using evaluation data
        lr_bigram_predicted = self.basic_logistic_regression(self.training_set.target,
                                                             BB_training_count,
                                                             BB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.lr_bigram, lr_bigram_predicted)
        # <---------- SVM Unigram ---------->
        # train the model, test it using evaluation data
        svm_unigram_predicted = self.basic_svm(self.training_set.target,
                                               UB_training_count,
                                               UB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.svm_unigram, svm_unigram_predicted)
        # <---------- SVM Bigram ---------->
        # train the model, test it using evaluation data
        svm_bigram_predicted = self.basic_svm(self.training_set.target,
                                              BB_training_count,
                                              BB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.svm_bigram, svm_bigram_predicted)
        # <---------- Random Forest Unigram ---------->
        # train the model, test it using evaluation data
        rf_unigram_predicted = self.basic_random_forest(self.training_set.target,
                                                        UB_training_count,
                                                        UB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.rf_unigram, rf_unigram_predicted)
        # <---------- Random Forest Bigram ---------->
        # train the model, test it using evaluation data
        rf_bigram_predicted = self.basic_random_forest(self.training_set.target,
                                                       BB_training_count,
                                                       BB_evaluation_count)
        # calculate scores based on predicted values
        self.populateScores(self.rf_bigram, rf_bigram_predicted)

    # Compute feature representation using count_vectorizer
    # return the feature representation of the given training and evaluation data
    def count_vectorizer(self, training_data, evaluation_data, n_gram):
        count_vectorizer = CountVectorizer(encoding='latin-1', ngram_range=n_gram)
        training_count = count_vectorizer.fit_transform(training_data)
        evaluation_count = count_vectorizer.transform(evaluation_data)
        return training_count, evaluation_count

    # This method applies the naive bayes classification method using the provided training data to train the model
    # and then uses the evaluation data to predict actual labels with the now trained model
    # returns predicted values
    def basic_naive_bayes(self, training_target, training_count, evaluation_count):
        classifier = MultinomialNB().fit(training_count, training_target)
        predicted = classifier.predict(evaluation_count)
        return predicted

    # This method applies the logistic regression classification method using the provided training data to train
    # the model and then uses the evaluation data to predict actual labels with the now trained model
    # returns predicted values
    def basic_logistic_regression(self, training_target, training_count, evaluation_count):
        classifier = LogisticRegression(max_iter=1000).fit(training_count, training_target)
        predicted = classifier.predict(evaluation_count)
        return predicted

    # This method applies the Support Vector Machines classification method using the provided training data to train
    # the model and then uses the evaluation data to predict actual labels with the now trained model
    # returns predicted values
    def basic_svm(self, training_target, training_count, evaluation_count):
        classifier = svm.LinearSVC(max_iter=100000).fit(training_count, training_target)
        predicted = classifier.predict(evaluation_count)
        return predicted

    # This method applies the Random Forests classification method using the provided training data to train
    # the model and then uses the evaluation data to predict actual labels with the now trained model
    # returns predicted values
    def basic_random_forest(self, training_target, training_count, evaluation_count):
        classifier = RandomForestClassifier(random_state=0).fit(training_count, training_target)
        predicted = classifier.predict(evaluation_count)
        return predicted

    # This function is used to claculate and set the precision score, recall score
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

    # This method is used to plot the learning curve whcih is a plot of the performance of the classifier
    # (F1- score on the y-axis) on the evaluation data, when trained on different amounts of training data
    # (size of training data on the x-axis). This performed for the unigram configuration of all 4 classifiers
    # (i.e for NB, LR, SVM, and RF)
    def plot_learning_curve(self, training_set, evaluation_set):
        trained_set_sizes = self.getTrainedData(training_set)
        train_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        # store the f1 scores of each classifier in the corresponding arrays for each size of the training data
        naives_bayes_f1_scores = []
        lr_f1_scores = []
        svm_f1_scores = []
        rf_f1_scores = []

        # get f1 scores for all 4 trained models (NB, LR, SVM, and RF) for each training data size
        # (sizes: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
        for (trained_data, trained_target) in trained_set_sizes:
            UB_training_count, UB_evaluation_count = self.count_vectorizer(trained_data,
                                                                           evaluation_set.data,
                                                                           n_gram=(1, 1))
            # <---------- Naive Bayes ---------->
            naive_bayes_unigram_predicted = self.basic_naive_bayes(trained_target,
                                                                   UB_training_count,
                                                                   UB_evaluation_count)
            # calculate f1
            nb_f1_score = sklearn.metrics.f1_score(evaluation_set.target,
                                                   naive_bayes_unigram_predicted,
                                                   average='macro')
            naives_bayes_f1_scores.append(nb_f1_score)
            # <---------- Logistic Regression ---------->
            lr_unigram_predicted = self.basic_logistic_regression(trained_target,
                                                                  UB_training_count,
                                                                  UB_evaluation_count)
            # calculate f1
            lr_f1_score = sklearn.metrics.f1_score(evaluation_set.target,
                                                   lr_unigram_predicted,
                                                   average='macro')
            lr_f1_scores.append(lr_f1_score)
            # <---------- Support Vector Machine ---------->
            svm_unigram_predicted = self.basic_svm(trained_target,
                                                   UB_training_count,
                                                   UB_evaluation_count)
            # calculate f1
            svm_f1_score = sklearn.metrics.f1_score(evaluation_set.target,
                                                    svm_unigram_predicted,
                                                    average='macro')
            svm_f1_scores.append(svm_f1_score)
            # <---------- RainForest ---------->
            rf_unigram_predicted = self.basic_random_forest(trained_target,
                                                            UB_training_count,
                                                            UB_evaluation_count)
            # calculate f1
            rf_f1_score = sklearn.metrics.f1_score(evaluation_set.target,
                                                   rf_unigram_predicted,
                                                   average='macro')
            rf_f1_scores.append(rf_f1_score)

        # plot learning curve
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=train_sizes, y=naives_bayes_f1_scores,
                                 mode='lines+markers',
                                 name='NB'))
        fig.add_trace(go.Scatter(x=train_sizes, y=lr_f1_scores,
                                 mode='lines+markers',
                                 name='LR'))
        fig.add_trace(go.Scatter(x=train_sizes, y=svm_f1_scores,
                                 mode='lines+markers',
                                 name='SVM'))
        fig.add_trace(go.Scatter(x=train_sizes, y=rf_f1_scores,
                                 mode='lines+markers',
                                 name='RF'))
        fig.update_layout(
            title="Learning Curve",
            xaxis_title="Size of Training Data (%)",
            yaxis_title="F1-Score",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        fig.show()

    # Given a training set, this mathod returns an array of tuples containing training data and training target
    # for each training size (sizes: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
    def getTrainedData(self, training_set):
        X_train_data_10, X_test_data_10, y_train_target_10, y_test_target_10 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.1,
                                                                                                test_size=0.9)
        X_train_data_20, X_test_data_20, y_train_target_20, y_test_target_20 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.2,
                                                                                                test_size=0.8)
        X_train_data_30, X_test_data_30, y_train_target_30, y_test_target_30 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.3,
                                                                                                test_size=0.7)
        X_train_data_40, X_test_data_40, y_train_target_40, y_test_target_40 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.4,
                                                                                                test_size=0.6)
        X_train_data_50, X_test_data_50, y_train_target_50, y_test_target_50 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.5,
                                                                                                test_size=0.5)
        X_train_data_60, X_test_data_60, y_train_target_60, y_test_target_60 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.6,
                                                                                                test_size=0.4)
        X_train_data_70, X_test_data_70, y_train_target_70, y_test_target_70 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.7,
                                                                                                test_size=0.3)
        X_train_data_80, X_test_data_80, y_train_target_80, y_test_target_80 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.8,
                                                                                                test_size=0.2)
        X_train_data_90, X_test_data_90, y_train_target_90, y_test_target_90 = train_test_split(training_set.data,
                                                                                                training_set.target,
                                                                                                train_size=0.9,
                                                                                                test_size=0.1)
        return [(X_train_data_10, y_train_target_10), (X_train_data_20, y_train_target_20),
                (X_train_data_30, y_train_target_30), (X_train_data_40, y_train_target_40),
                (X_train_data_50, y_train_target_50), (X_train_data_60, y_train_target_60),
                (X_train_data_70, y_train_target_70), (X_train_data_80, y_train_target_80),
                (X_train_data_90, y_train_target_90), (self.training_set.data, self.training_set.target)]
