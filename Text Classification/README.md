#Text Classification
This project investigates the utility of different
learning algorithms for a text classification task. 
The project uses the implementations available in the 
scikit python library. The plotly library is used to 
visualize the performances of the used classifiers.

The classifiers are trained to classify input texts 
into one of the K-classes. The classifiers have three 
configurations:
- Unigram Baseline (UB) – Basic sentence segmentation 
  and tokenization. Use all words.
- Bigram Baseline (BB) – Use all bigrams.
  (e.g. I ran a race => I ran, ran a, a race.)
- My best configuration (MBC) - Uses the best configuration 
  of the used classifiers (the configurations that have the 
  best evaluation scores).
###Used Classifiers
- Naive Bayes
- Logistic Regression  
- Support Vector Machines 
- Random Forests

##Provided Data Set 
The “20 newsgroup dataset” is provided in the project, which 
contains 20,000 newsgroup documents partitioned into 20 news 
categories. We treat each of the categories as classes.
In each class, there two sets of documents, one for training and one for test.

##Basic Comparison with Baselines

- For all four methods (Naive Bayes, Logistic Regression, Support Vector Machines, and Random Forests), 
  Basic Comparison runs both unigram and bigram baselines.
  
###To Run:
```bash
python UB_BB.py <trainset> <evalset> <output> <display LC>
```
- "trainset" is the parent folder to your training data 
and "evalset" is the parent folder to your evaluation data.
For the example shown in the figure below, <trainset> should be ‘Training’, 
and "evalset" should be ‘Evaluation’.

-  "display LC" is an option to display the learning curve. ‘1’ to show the plot, ‘0’ to NOT show the plot. 
    - A learning curve (LC) result, where you show the performance of each classifier only with the unigram 
      representation. The learning curve is a plot of the performance of the classifier (F1- score on the y-axis) 
      on the evaluation data, when trained on different amounts of training data (size of training data on the x-axis).

- "output" is the path to a comma-separated values file, which contains 8 lines corresponding to 8 runs. Each line is 
  "Classification Method", "Configuration", "Macro-Precision", "Macro-Recall", "F1-score", evaluated on 
  the evaluation data.

##My Best Configuration
After observing the performances of the basic versions of the all four classification methods,
I added some improvements for each classification method to increase their accuracy,
precision and f1 scores.
###Naive Bayes Design Choices 
- Used Count Vectorizer to improve evaluation scores on test data
- Added feature selection using Select From Model method
- Used stemming, ignoring stop words and lower casing words
###Logistic Regression Design Choices
- Used Count Vectorizer to improve evaluation scores on test data
- Added feature selection using Select From Model method
- Used stemming, ignoring stop words and lower casing words
###Support Vector Machines Design Choices
- Used TFIDF to improve evaluation scores on test data
- Added feature selection using Select From Model method
- Used stemming, ignoring stop words and lower casing words
###Random Forests Design Choices
- Used TFIDF to improve evaluation scores on test data  
- Added feature selection using Select From Model method
- Used stemming, ignoring stop words and lower casing words

###To Run
```bash
python MBC_exploration.py <trainset> <evalset> <output>
```
- The output file contains 4 lines. Each line is
```bash
  <Classification Method>, <Configuration>, <Macro-Precision>, <Macro-Recall>, <F1-score>
 ```
- where "Classification Method" is  one of {NB, LR, SVM, RF}. The content of the output file for the NewsGroup 
  Dataset is included in the Report.pdf file.

##My Best Configuration Final
Improved Naive Bayes gave me the highest evaluation scores,
which is why I provided it as my final MBC.
###To Run
```bash
python MBC_final.py <trainset> <testset> <output>
```
The output file contains a single line evaluated on the test data in the same format as previous ones.