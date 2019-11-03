import pandas as pd
from absl import app
from absl import flags
import csv
import collections
import json

FLAGS = flags.FLAGS

flags.DEFINE_string('good_file', '/Users/JasminH/hacknlead2019/Data/ListofGoodsExcel.tsv',
                    '.tsv file to extract data from')
flags.DEFINE_string('GSI_file', '/Users/JasminH/hacknlead2019/Data/GSI_data.csv', '.tsv file to extract data from')
flags.DEFINE_string('prevention_file', '/Users/JasminH/hacknlead2019/Data/slavery_prevention_scores.csv',
                    '.tsv file to extract data from')
flags.DEFINE_string('product_json', '/Users/JasminH/hacknlead2019/Data/products.json',
                    '.json file to convolute the data in')
flags.DEFINE_string('country_json', '/Users/JasminH/hacknlead2019/Data/countries.json',
                    '.json file to convolute the data in')



class MergeData:
    'A Class to merge data from different sources into.'

    def __init__(self):
        # Map products to countries
        self.products = collections.defaultdict(list)
        # Map countries to scores
        self.countries = {}

    def read_good_csv(self, f):
        """ Extract goods and human trafficking evidence from list of goods.

        :param f: file with list of goods, countries of origin, and crimes.
        """

        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)

            for row in rows:
                if row['good'] in self.products:
                    self.products[row['good']].append(
                        row['country'])  # = {'forced_labor': forced_labor, 'child_labor': child_labor}
                else:
                    self.products[row['good']] = [row['country']]
                if row['country'] in self.countries:
                    if row['child_labor'] == 'X':
                        self.countries[row['country']]['c_f_labor'] += 1
                    if row['forced_labor'] == 'X':
                        self.countries[row['country']]['c_f_labor'] += 1
                else:
                    self.countries[row['country']] = {'c_f_labor': 0}
                    if row['child_labor'] == 'X':
                        self.countries[row['country']]['c_f_labor'] += 1
                    if row['forced_labor'] == 'X':
                        self.countries[row['country']]['c_f_labor'] += 1

    def read_prevention(self, f):
        """Get achieved % of prevention goals for countries in list of good from prevention measurements."""
        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                if row['Country'] in self.countries:
                    self.countries[row['Country']]['prevention_percentage_total'] = row['TOTAL % ROUND']
                else:
                    continue

    def read_gsi(self, f):
        """Get scores that map to countries in list of goods from the GSI."""
        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                # print(row)
                if row['country'] in self.countries:
                    self.countries[row['country']]['prevalence_score'] = row['prevalence_score']
                    self.countries[row['country']]['people_in_slavery'] = row['people_in_slavery']
                    self.countries[row['country']]['vulnerability_score'] = row['vulnerability_score']
                    self.countries[row['country']]['support_survivors_percentage'] = row[
                        'support_survivors_percentage']
                    self.countries[row['country']]['criminal_justice_percentage'] = row[
                        'criminal_justice_percentage']
                    self.countries[row['country']]['coordination_percentage'] = row['coordination_percentage']
                    self.countries[row['country']]['address_risk_percentage'] = row['address_risk_percentage']
                    self.countries[row['country']]['supply_chains_percentage'] = row['supply_chains_percentage']
                    self.countries[row['country']]['TOTAL'] = row['TOTAL']

                if ',' in row['country']:
                    country, _ = row['country'].split(',')
                    if country in self.countries:
                        self.countries[country]['prevalence_score'] = row['prevalence_score']
                        self.countries[country]['people_in_slavery'] = row['people_in_slavery']
                        self.countries[country]['vulnerability_score'] = row['vulnerability_score']
                        self.countries[country]['support_survivors_percentage'] = row[
                            'support_survivors_percentage']
                        self.countries[country]['criminal_justice_percentage'] = row[
                            'criminal_justice_percentage']
                        self.countries[country]['coordination_percentage'] = row['coordination_percentage']
                        self.countries[country]['address_risk_percentage'] = row['address_risk_percentage']
                        self.countries[country]['supply_chains_percentage'] = row[
                            'supply_chains_percentage']
                        self.countries[country]['TOTAL'] = row['TOTAL']

                    else:
                        continue
                else:
                    continue


def main(argv):

    merge_data = MergeData()
    merge_data.read_good_csv(FLAGS.good_file)
    merge_data.read_prevention(FLAGS.prevention_file)
    merge_data.read_gsi(FLAGS.GSI_file)

    with open(FLAGS.country_json, 'w') as cf:
        json.dump(merge_data.countries, cf)
    with open(FLAGS.product_json, 'w') as pf:
        json.dump(merge_data.products, pf)


if __name__ == '__main__':
    app.run(main)
