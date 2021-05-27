import sys
import sklearn as sklearn
from sklearn import datasets
from MBC_Comparison import MBC_Comparison


# This function is called to write the scores of Naive Bayes for
# My Best Configuration to the provided output file
def write_output(output_file, mbc_comparison):
    output_file.write(mbc_comparison.nb.name)
    output_file.write(',')
    output_file.write(mbc_comparison.nb.n_gram)
    output_file.write(',')
    output_file.write(str(mbc_comparison.nb.macro_precision))
    output_file.write(',')
    output_file.write(str(mbc_comparison.nb.macro_recall))
    output_file.write(',')
    output_file.write(str(mbc_comparison.nb.f1_score))


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
    mbc.naive_bayes_MBC()

    # write the evaluation scores to the file
    write_output(out_file, mbc)

    out_file.close()
