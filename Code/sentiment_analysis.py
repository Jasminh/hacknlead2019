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
flags.DEFINE_string('output_json', '/Users/JasminH/hacknlead2019/Data/countries_with_articles.json',
                    '.tsv file to extract data from')
flags.DEFINE_string('country_json', '/Users/JasminH/hacknlead2019/Data/countries.json',
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
    """Class that adds sentiment enriched news articles to pre-existing json files by country"""

    def __init__(self, f):
        # information on countries to be complemented with news
        self.countries = json.load(open(f))

    def get_news(self, f):
        """Get news articles from tsv and do sentiment analysis on the articles"""
        with open(f) as texts:
            rows = csv.DictReader(texts, delimiter='\t')
            for row in rows:
                row = sentiment_analysis(row)
                self.merge_data(row)

    def merge_data(self, row):
        """Get list of countries associated with the news articles and associate articles with countries in the json."""
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
    add_sentiments = AddSentiments(FLAGS.country_json)
    add_sentiments.get_news(FLAGS.text_file)
    with open(FLAGS.output_json, 'w') as json_f:
        json.dump(add_sentiments.countries, json_f)


if __name__ == '__main__':
    app.run(main)
