# Quantifying-Mental-Health-Signals-on-Twitter
Group 14 COMP-5111FA
Adhri Nandini Paul - 0885302
Lakshman Boddu - 0885377
Vishal Sheshadri - 0888758

Prerequisite software:
Anaconda - https://www.anaconda.com/download/ 
	Or
Python 3.7 - https://www.python.org/downloads/ 	

Libraries used:
numpy 
Tweepy
TwitterSearch API
Scikit-learn
Linguistic Inquiry Word Count (LIWC) 2015

Installing Numpy:
Run the following code in terminal:
 Python -m pip install -user numpy

Installing tweepy:
Run the following code in terminal:
pip install tweepy

Installing TwitterSearch API:
Run the following code in terminal:
pip install TwitterSearch

Installing scikit-learn:
Run the following code in terminal:
pip install scikit-learn

Installing LIWC:
LIWC Packages are included in our code and need not be downloaded. They are automatically included once the code is downloaded or cloned. The files named word_category_counter.py and LIWC2015_English_Flat.dic are part if the LIWC package.

Code and output files:
Code for our project can be found at: https://github.com/lakshmanboddu/Quantifying-Mental-Health-Signals-on-Twitter 

Steps for working the project using Anaconda Application:
Clone or download the code from the above link to your computer.
Launch the jupyter notebook from the menu.
Open the respective folder to which you downloaded the code repository.
Double-click keyword_search_tweets.py to run it and collect tweets for each disorder.
After running the code, a file named Data.csv will be generated.
Double-click on Data_processing.py to run it and perform LIWC analysis.
After running Data_processing.py, a file named dataset_features_test.csv will be generated.
Double-click on Collect_tweets.py to run it to collect tweets.
After running Collect_tweets.py, a file named Merged_all_fornow.csv will be generated.
Repeat step 5 to obtain a file named dataset_features.csv.
Double-click on Logistic_regression.py to run it to perform prediction.
After running Logistic_regression.py, a file named prediction_tweets.py will be generated. This is the final output with a tweet and respective disorder predicted to it.

Steps for working the project if not using Anaconda and just using Python:
Clone or download the code from the above link to your computer.
Open pre-installed terminal application if using a macOS, unix or Linux based operating system or open command prompt application if using Windows.
Run keyword_search_tweets.py to collect tweets for each disorder. 
Run the command python keyword_search_tweets.py
After running the code, a file named Data.csv will be generated.
Afterward, we would pass this csv file through LIWC. For that reason you have to run Data_processing.py. This file will work in the presence of  word_category_counter.py and LIWC2015_English_Flat.dic in the home directory.
Run the command python Data_processing.py
After running Data_processing.py, a file named dataset_features_test.csv will be generated. 
To predict how our model works on random dataset, run the Collect_tweets.py to collect tweets by using username and store tweets in Merged_all_fornow.csv . 
Run the command python Collect_tweets.py
Afterward , you would follow step 5 and stored the dataset in  dataset_features.csv.
To train our model with logistic regression, we need to run Logistic_regression.py. 
Run the command python Logistic_regression.py
After running Logistic_regression.py, we would get prediction_tweets.csv. This is the file where  prediction of model on unknown dataset has been stored.
