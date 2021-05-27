import sys
import sklearn as sklearn
from sklearn import datasets
from MBC_Comparison import MBC_Comparison


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
# Vector Machines, and Random Forests) for My Best Configuration to the provided output file
def write_output(output_file, mbc_comparison):
    for i in range(0, len(mbc_comparison.myMethods)):
        writeScores(output_file, mbc_comparison.myMethods[i])
        if i != (len(mbc_comparison.myMethods) - 1):
            output_file.write('\n')

if __name__ == '__main__':
    out_file = ''

    trainset = sys.argv[1]
    evalset = sys.argv[2]
    out_file = open(sys.argv[3], 'w')

    labels = ['rec.sport.hockey', 'sci.med', 'soc.religion.christian', 'talk.religion.misc']

    training_set = sklearn.datasets.load_files(trainset, categories=labels, load_content=True,
                                               shuffle=True, random_state=0)

    evaluation_set = sklearn.datasets.load_files(evalset, categories=labels, load_content=True,
                                                 shuffle=True, random_state=0)

    # Train modals of 4 classifications using MBC and evaluate them and calculate their scores
    mbc = MBC_Comparison(training_set, evaluation_set)
    mbc.apply_mbc()

    # write the evaluation scores to the file
    write_output(out_file, mbc)
    out_file.close()
