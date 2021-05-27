# This class presents a classification method and is used as a convenience for outputting name, n_gram,
# macro_precision score, macro_recall score, and f1 score of the classification method (i.e Naive Bayes,
# Logistic Regression, Support # Vector Machines, or Random Forests)
class classificationMethod:
    def __init__(self, name, macro_precision, macro_recall, f1_score, n_gram):
        self.name = name
        self.macro_precision = macro_precision
        self.macro_recall = macro_recall
        self.f1_score = f1_score
        self.n_gram = n_gram

    def setPrecision(self, new_precision):
        self.macro_precision = new_precision

    def setRecall(self, new_recall):
        self.macro_recall = new_recall

    def setF1(self, new_f1_score):
        self.f1_score = new_f1_score