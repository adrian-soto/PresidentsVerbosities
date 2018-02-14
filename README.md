# Presidents' Verbosities
An look into the State of the Union addresses of Barack Obama in 2010 and Donald Trump in 2018 using visualization and NLP techniques.

Text sources:
  - http://www.cnn.com/2010/POLITICS/01/27/sotu.transcript/index.html
  - https://www.rawstory.com/2018/01/trumps-state-of-the-union-speech-full-text/

Note: Obama's original transcription was slightly cleaned up for ease of this study. In particular, comments such as "(APPLAUSE)" or "(LAUGHTER)" were removed and the sentences that were interrupted either by the public or by a mistake were sown back together.


## Getting started
In this repository one can find the main jupyter notebooks
  - wordclouds.ipynb
  - sentiments.ipynb
The first one is used to generate wordclouds from the input text, while the second one is used for a sentiment analysis.

### Prerequisites

This code is Python 2.7 and requires the following packages:

 - matplotlib
 - wordcloud
 - nltk

Please ensure these packages are installed before attempting to run this code


## RESOURCES

  - wordcloud package repo and simple example:
    https://github.com/amueller/word_cloud/blob/master/README.md	
    https://github.com/amueller/word_cloud/blob/master/examples/simple.py

  - fancier examples with wordcloud 
    http://minimaxir.com/2016/05/wordclouds/

 - NLTK documentation: 
       http://www.nltk.org/api/nltk.sentiment.html

 - Original academic reference:
       http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf

 - Simple and practical explanation of VADER: 
       http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html

