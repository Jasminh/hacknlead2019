"""
Module add polarity scores to news articles and add them to an existing json.

Author: Jasmin Heierli

Project: hacknlead2019 / The Good Explorers
"""


import csv
import json
from absl import app
from absl import flags
import textblob
import nltk

FLAGS = flags.FLAGS

flags.DEFINE_string('text_file', '/Users/JasminH/hacknlead2019/Data/TR_API_files/TR_API_results.tsv',
                    '.tsv file to extract data from')


def sentiment_analysis(row):
    text = row['parsed_text'].replace('\n', ' ')
    sentences = nltk.tokenize.sent_tokenize(text)
    scores = []
    for sentence in sentences:
        blob = textblob.TextBlob(sentence)
        scores.append(blob.sentiment[0])
    dist = (0 - max(scores))
    if dist < min(scores):
        polarity = max(scores)
    else:
        polarity = min(scores)

    row['polarity'] = polarity
    row['polarity_sentence_scores'] = scores

    return row


class AddSentiments:

    def __init__(self, f):
        self.countries = json.load(open(f))

    def get_news(self, f):
        with open(f) as texts:
            rows = csv.DictReader(texts, delimiter='\t')
            for row in rows:
                row = sentiment_analysis(row)
                crs = row['countries_long_newversion'].split(',')
                for country in crs:
                    if 'articles' in self.countries[country]:
                        self.countries[country]['articles'][row['versionedguid']] = {'date': row['firstcreated'],
                                                                                     'text': row['parsed_text'],
                                                                                'polarity': row['polarity'],
                                                                                'polarity_sentence_scores': row[
                                                                                    'polarity_sentence_scores']}
                    else:
                        self.countries[country]['articles'] = {
                            row['versionedguid']: {'date': row['firstcreated'], 'text': row['parsed_text'],
                                                   'polarity': row['polarity'],
                                                   'polarity_sentence_scores': row['polarity_sentence_scores']}}





def main(argv):
    add_sentiments = AddSentiments('/Users/JasminH/hacknlead2019/Data/countries.json')
    add_sentiments.get_news(FLAGS.text_file)
    with open('/Users/JasminH/hacknlead2019/Data/countries_with_articles.json', 'w') as json_f:
        json.dump(add_sentiments.countries, json_f)


if __name__ == '__main__':
    app.run(main)
