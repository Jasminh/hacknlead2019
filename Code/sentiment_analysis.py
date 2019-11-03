import csv
import json
from absl import app
from absl import flags
import textblob
import nltk

FLAGS = flags.FLAGS

flags.DEFINE_string('text_file', '/Users/JasminH/hacknlead2019/Data/TR_API_results.tsv',
                    '.tsv file to extract data from')


def get_news(f, countries):
    with open(f) as texts:
        rows = csv.DictReader(texts, delimiter='\t')
        print(countries)
        for row in rows:
            row = sentiment_analyis(row)
            crs = row['countries_long'].split(',')
            for country in crs:
                print(country)
                try:
                    if 'articles' in countries[country]:
                        pass
                    else:
                        countries[country]['articles'] = {'guid': row['versionedguid']}
                except:
                    print('****OLD VERSION*****')


def sentiment_analyis(row):
    text = row['parsed_text'].replace('\n', ' ')
    sentences = nltk.tokenize.sent_tokenize(text)
    scores = []
    for sentence in sentences:
        blob = textblob.TextBlob(sentence)
        scores.append(blob.sentiment[0])
    dist = (0 - max(scores))
    if dist > min(scores):
        polarity = max(scores)
    else:
        polarity = min(scores)
    # print(polarity)

    row['polarity'] = polarity
    print(row)

    return row


def get_countries(f):
    with open(f) as countries:
        data = json.load(countries)
        return data


def main(argv):
    countries = get_countries('/Users/JasminH/hacknlead2019/Data/countries.json')
    get_news(FLAGS.text_file, countries)


if __name__ == '__main__':
    app.run(main)
