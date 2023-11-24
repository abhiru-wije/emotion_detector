#text preprocessing
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
def preprocess(line):
    ps = PorterStemmer()

    review = re.sub('[^a-zA-Z]', ' ', line) 
    review = review.lower() 
    review = review.split() 

    review = [ps.stem(word) for word in review if not word in stopwords.words('english')] 
    return " ".join(review)
