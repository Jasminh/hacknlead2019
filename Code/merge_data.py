import pandas as pd
from absl import app
from absl import flags
import csv
import collections

FLAGS = flags.FLAGS

flags.DEFINE_string('good_file', '/Users/JasminH/hacknlead2019/Data/ListofGoodsExcel.tsv',
                    '.tsv file to extract data from')
flags.DEFINE_string('GSI_file', '/Users/JasminH/hacknlead2019/Data/GSI_data.csv', '.tsv file to extract data from')
flags.DEFINE_string('slavery_file', '/Users/JasminH/hacknlead2019/Data/slavery_vulnerability_index.tsv',
                    '.tsv file to extract data from')
flags.DEFINE_string('prevention_file', '/Users/JasminH/hacknlead2019/Data/slavery_prevention_scores.tsv',
                    '.tsv file to extract data from')
flags.DEFINE_list('column_names', 'good,country', 'List of columns to extract from TSV')
flags.DEFINE_string('output_file', None, '.tsv file to convolute the data in')


class MergeData:

    def __init__(self):
        self.products = collections.defaultdict(list)
        self.countries = {}

    def read_good_csv(self, f):
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

    def read_csv(self, f, columns):
        with open(f, encoding='latin-1') as csv_file:
            rows = csv.DictReader(csv_file, delimiter='\t')
            for row in rows:
                # print(row)
                if row['Country'] in self.countries:
                    self.countries[row['Country']]['vulnerability_index'] = row['Overall_weighted_average']
                else:
                    continue

    def read_gsi(self, f, columns):
        with open(f) as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                # print(row)
                if row['country'] in self.countries:
                    self.countries[row['country']][row['prevalence_score']] = row['prevalence_score']
                    self.countries[row['country']][row['people_in_slavery']] = row['people_in_slavery']
                    self.countries[row['country']][row['vulnerability_score']] = row['vulnerability_score']
                    self.countries[row['country']][row['support_survivors_percentage']] = row[
                        'support_survivors_percentage']
                    self.countries[row['country']][row['criminal_justice_percentage']] = row[
                        'criminal_justice_percentage']
                    self.countries[row['country']][row['coordination_percentage']] = row['coordination_percentage']
                    self.countries[row['country']][row['address_risk_percentage']] = row['address_risk_percentage']
                    self.countries[row['country']][row['supply_chains_percentage']] = row['supply_chains_percentage']
                    self.countries[row['country']][row['TOTAL']] = row['TOTAL']
                if row['country'] == 'Russian Federation':
                    self.countries['Russia'][row['prevalence_score']] = row['prevalence_score']
                    self.countries['Russia'][row['people_in_slavery']] = row['people_in_slavery']
                    self.countries['Russia'][row['vulnerability_score']] = row['vulnerability_score']
                    self.countries['Russia'][row['support_survivors_percentage']] = row[
                        'support_survivors_percentage']
                    self.countries['Russia'][row['criminal_justice_percentage']] = row[
                        'criminal_justice_percentage']
                    self.countries['Russia'][row['coordination_percentage']] = row['coordination_percentage']
                    self.countries['Russia'][row['address_risk_percentage']] = row['address_risk_percentage']
                    self.countries['Russia'][row['supply_chains_percentage']] = row[
                        'supply_chains_percentage']
                if ',' in row['country']:
                    country, _ = row['country'].split(',')
                    if country in self.countries:
                        self.countries[country][row['prevalence_score']] = row['prevalence_score']
                        self.countries[country][row['people_in_slavery']] = row['people_in_slavery']
                        self.countries[country][row['vulnerability_score']] = row['vulnerability_score']
                        self.countries[country][row['support_survivors_percentage']] = row[
                            'support_survivors_percentage']
                        self.countries[country][row['criminal_justice_percentage']] = row[
                            'criminal_justice_percentage']
                        self.countries[country][row['coordination_percentage']] = row['coordination_percentage']
                        self.countries[country][row['address_risk_percentage']] = row['address_risk_percentage']
                        self.countries[country][row['supply_chains_percentage']] = row[
                            'supply_chains_percentage']
                        self.countries[country][row['TOTAL']] = row['TOTAL']

                    else:
                        continue
                else:
                    continue

def main(argv):
    merge_data = MergeData()
    merge_data.read_good_csv(FLAGS.good_file)
    merge_data.read_csv(FLAGS.slavery_file, FLAGS.column_names)
    merge_data.read_gsi(FLAGS.GSI_file, FLAGS.column_names)
    # for k, v in merge_data.products.items():
    # print(k, v)
    print(merge_data.countries)
    print(merge_data.products)
    count_missing = 0
    for k, v in merge_data.countries.items():
        if len(v) < 3:
            print(k)
            count_missing += 1
    print(count_missing)


if __name__ == '__main__':
    app.run(main)
