# Ben Haws
# 9/22/2021
# DATA51100
# Fall 2021
# Programming Assignment 4: ProbEst

from pandas import DataFrame
import pandas as pd


def main():
    intro = 'DATA51100, FALL 2021\nNAME: Ben Haws\nPROGRAMMING ASSIGNMENT#4\n'
    print(intro)

    # import cars data as DataFrame & select make & aspiration columns
    car_data = pd.read_csv('cars.csv')[['make', 'aspiration']]

    # create empty data frame in the correct shape to fill
    car_stats = DataFrame()
    car_stats.index = set(car_data['make'])
    car_stats.index.name = 'make'

    # create series of total models for each make and join to main df
    total = car_data.value_counts(subset='make', sort=False)
    total.name = 'total'
    total = DataFrame(total)
    car_stats = pd.merge(car_stats, total, left_index=True, right_index=True)

    # create a series of total standard models for each make and merge
    std = car_data[car_data['aspiration'] == 'std'].value_counts(sort=False)
    std = std.to_frame()

    # cleans up the dataframe, leaving a one column frame ready to merge
    std.reset_index(inplace=True)
    std.drop('aspiration', axis=1, inplace=True)
    std.rename(columns={0: 'std'}, inplace=True)
    std.set_index('make', inplace=True)

    # merge into car_stats--outer merge keeps makes with no std models
    car_stats = pd.merge(car_stats, std, how='outer', left_index=True, right_index=True)
    car_stats.fillna(0, inplace=True)

    # create a series of total turbo models for each make and merge
    turbo = car_data[car_data['aspiration'] == 'turbo'].value_counts(sort=False)
    turbo = turbo.to_frame()

    # cleans up the dataframe, leaving a one column frame ready to merge
    turbo.reset_index(inplace=True)
    turbo.drop('aspiration', axis=1, inplace=True)
    turbo.rename(columns={0: 'turbo'}, inplace=True)
    turbo.set_index('make', inplace=True)

    # merge into car_stats--outer merge keeps makes with no turbo models
    car_stats = pd.merge(car_stats, turbo, how='outer', left_index=True, right_index=True)
    car_stats.fillna(0, inplace=True)

    # add columns for probabilities
    car_stats['prob std'] = car_stats['std'] / car_stats['total'] * 100
    car_stats['prob turbo'] = car_stats['turbo'] / car_stats['total'] * 100

    # format and print probabilities for aspiration vs model
    for label, row in car_stats.iterrows():
        print('Prob(aspiration=std|make=', label, ') = ', '{:.2f}'.format(row['prob std']), '%')
        print('Prob(aspiration=turbo|make=', label, ') = ', '{:.2f}'.format(row['prob turbo']), '%')

    # Get value counts for make and total of all make, then calculate probabilities for each make
    total = car_data['make'].value_counts(sort=False).sum()
    car_stats['prob make'] = car_data['make'].value_counts(sort=False) / total * 100

    # Print make probabilities
    print('\n')
    for index, prob in car_stats['prob make'].items():
        print('Prob(make = ', index, ') = ', '{:.2f}'.format(prob), '%')

    return


if __name__ == '__main__':
    main()
