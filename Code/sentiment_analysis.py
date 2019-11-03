import csv
import json
from absl import app
from absl import flags
import textblob
import nltk

FLAGS = flags.FLAGS

flags.DEFINE_string('text_file', '/Users/JasminH/hacknlead2019/Data/TR_API_files/TR_API_results.tsv',
                    '.tsv file to extract data from')


def get_news(f, countries):
    with open(f) as texts:
        rows = csv.DictReader(texts, delimiter='\t')
        for row in rows:
            row = sentiment_analyis(row)
            crs = row['countries_long_newversion'].split(',')
            for country in crs:
                if 'articles' in countries[country]:
                    countries[country]['articles'][row['versionedguid']] = {'text': row['parsed_text'],
                                                                                'polarity': row['polarity'],
                                                                                'polarity_sentence_scores': row[
                                                                                    'polarity_sentence_scores']}
                else:
                    countries[country]['articles'] = {
                        row['versionedguid']: {'text': row['parsed_text'], 'polarity': row['polarity'],
                                                   'polarity_sentence_scores': row['polarity_sentence_scores']}}
            return countries


def sentiment_analyis(row):
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


def get_countries(f):
    with open(f) as countries:
        data = json.load(countries)
        return data


def main(argv):
    countries = get_countries('/Users/JasminH/hacknlead2019/Data/countries.json')
    updated_countries = get_news(FLAGS.text_file, countries)
    with open('/Users/JasminH/hacknlead2019/Data/countries_with_articles.json', 'w') as json_f:
        json.dump(updated_countries, json_f)


if __name__ == '__main__':
    app.run(main)
