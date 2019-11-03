import csv
import json
from absl import app
from absl import flags
from pycorenlp import StanfordCoreNLP
import textblob
import nltk

FLAGS = flags.FLAGS

flags.DEFINE_string('text_file', '/Users/JasminH/hacknlead2019/Data/texts_api.csv',
                    '.tsv file to extract data from')


def get_news(f):
    with open(f) as texts:
        rows = csv.DictReader(texts)
        for row in rows:
            sentiment_analyis(row)
            # print(row['parsed_text'])


def sentiment_analyis(row):
    text = row['parsed_text'].replace('\n', ' ')
    sentences = nltk.tokenize.sent_tokenize(text)
    scores = []
    for sentence in sentences:
        blob = textblob.TextBlob(sentence)
        scores.append(blob.sentiment[0])
    polarity_avg = polarity_score / len(sentences)
    dist = (0 - max(scores))
    if dist > min(scores):
        polarity = max(scores)
    else:
        polarity = min(scores)
    print(polarity)


def main(argv):
    get_news(FLAGS.text_file)


if __name__ == '__main__':
    app.run(main)
