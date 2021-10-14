# Ben Haws
# DATA51100 Fall 2021
# Programming Assignment 7: Aggregating ACS PUMS Data
# using python

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# compute group statistics, for use with groupby.apply
def sum_stats(group):
    return {'mean': group.mean(), 'std': group.std(),  'count': group.count(),
            'min': group.min(), 'max': group.max()}


# compute group statistics for 3rd table
def stats2(group):
    return {'min': group.min(), 'max': group.max(), 'mean': group.mean()}


def main():

    pums = pd.read_csv('ss13hil.csv')[['HHT', 'HINCP', 'HHL', 'ACCESS', 'WGTP']]

    # slice income and family type, group and get stats
    income_vs_type = pums[['HINCP', 'HHT']]
    grouped_in = income_vs_type.HINCP.groupby(income_vs_type.HHT)
    in_type_sum = grouped_in.apply(sum_stats).unstack()

    # Set indices to be names of HHT values. Looks ugly, can't prettify
    in_type_sum.index = ['Married couple household', 'Nonfamily household:Male householder:Not living alone', 'Nonfam ily household:Female householder:Not living alone', 'Other family household:Male householder, no wife present', 'Other family household:Female householder, no husband present', 'Nonfamily household:Male householder:Living alone', 'Nonfamily household:Female householder:Living alone']
    in_type_sum.index.name = 'HHT - Household/family type'

    # Print 1st table
    header = '***Table 1 Descriptive Statistics of HINCP, grouped by HHT***'
    print(header)
    print(in_type_sum)

    # slice language and access data, initialize labels for table
    lang_acc = pums[['HHL', 'ACCESS', 'WGTP']].dropna()
    lang_index = ['English only', 'Spanish', 'Other Indo-European languages',
                  'Asian and Pacific Island languages', 'Other language', 'All']
    access1 = 'Yes w/ Subsrc.'
    access2 = 'Yes w/o Subsrc.'
    access3 = 'No'
    total = lang_acc.WGTP.sum()

    # crosstabulate and take the mean of all values
    lang_acc = pd.crosstab(lang_acc.HHL, lang_acc.ACCESS, lang_acc.WGTP, aggfunc='sum', margins=True)
    lang_acc = lang_acc / total  # using sum and then dividing by total WGTP

    # Set correct names for index and columns
    lang_acc.index = lang_index
    lang_acc.rename(columns={1.0: access1, 2.0: access2, 3.0: access3}, inplace=True)

    # Format table to percent at 2 decimal places
    pd.options.display.float_format = '{:.2%}'.format

    # Print 2nd table and reset formatting
    print('\n*** Table 2 - HHL vs. ACCESS - Frequency Table ***')
    print(lang_acc)
    pd.reset_option('display.float_format')

    # Slice income data and put into buckets
    in_quant = pums[['HINCP', 'WGTP']].dropna()
    labels = ['low', 'medium', 'high']
    quant = pd.qcut(in_quant.HINCP, 3, labels=labels)
    table3 = in_quant.HINCP.groupby(quant).apply(stats2).unstack()

    # join with household count data
    house_count = in_quant.WGTP.groupby(quant).apply(sum)
    house_count.name = 'household_count'
    table3 = table3.join(house_count)

    # Print income quantile analysis
    print('\n*** Quantile Analysis of HINCP - Household income (past 12 months) ***')
    print(table3)
    return


if __name__ == '__main__':
    print('DATA-51100, Fall 2021\nNAME: Ben Haws\nPROGRAMMING ASSIGNMENT #7\n')
    main()
