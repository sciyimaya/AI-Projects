import sys
import sklearn as sklearn
from sklearn import datasets
from BasicComparison import BasicComparison


# This function writes the name, n_gram method, macro precision score, macro recall score and f1 score
# of the provided classification method to the provided output file in a comma separated format
def writeScores(output_file, classification_method):
    output_file.write(classification_method.name)
    output_file.write(',')
    output_file.write(classification_method.n_gram)
    output_file.write(',')
    output_file.write(str(classification_method.macro_precision))
    output_file.write(',')
    output_file.write(str(classification_method.macro_recall))
    output_file.write(',')
    output_file.write(str(classification_method.f1_score))


# This function is called to write the scores of each classification method (Naive Bayes, Logistic Regression, Support
# Vector Machines, and Random Forests) for Unigram and Bigram baselines to the provided output file
def write_output(output_file, basic_comp):
    for i in range(0, len(basic_comp.myMethods)):
        writeScores(output_file, basic_comp.myMethods[i])
        if i != (len(basic_comp.myMethods) - 1):
            output_file.write('\n')


if __name__ == '__main__':
    out_file = ''

    trainset = sys.argv[1]
    evalset = sys.argv[2]
    out_file = open(sys.argv[3], 'w')
    # option to display learning curve
    display_LC = int(sys.argv[4])

    labels = ['rec.sport.hockey', 'sci.med', 'soc.religion.christian', 'talk.religion.misc']

    training_set = sklearn.datasets.load_files(trainset, categories=labels, load_content=True,
                                               shuffle=True, random_state=0)

    evaluation_set = sklearn.datasets.load_files(evalset, categories=labels, load_content=True,
                                                 shuffle=True, random_state=0)
    # apply all 4 methods, each with 2 configurations
    basic_comparison = BasicComparison(training_set, evaluation_set)
    basic_comparison.applyBasicComparison()
    # write the evaluation scores to the file
    write_output(out_file, basic_comparison)

    # optionally show learning curve
    if display_LC == 1:
        basic_comparison.plot_learning_curve(training_set, evaluation_set)

    out_file.close()
