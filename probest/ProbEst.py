# Ben Haws
# 9/22/2021
# DATA51100
# Fall 2021
# Programming Assignment 4: ProbEst

import pandas as pd


def main():
    intro = 'DATA51100, FALL 2021\nNAME: Ben Haws\nPROGRAMMING ASSIGNMENT#4'
    print(intro)

    # import cars data as DataFrame & select make & aspiration columns
    car_data = pd.read_csv('cars.csv')[['make', 'aspiration']]

    # create a series listing total cars of each make
    totals = car_data.value_counts(subset=['make'], sort=False)

    # create a series listing total cars of each aspiration for each make
    type_totals = car_data.value_counts(subset=['make', 'aspiration'], sort=False)  # FIXME: need to show rows with 0 of a type

    # join these series into DataFrame, add column for probability
    type_totals.name = 'type totals'  # add name to allow DataFrame operations
    totals.name = 'totals'

    totals = type_totals.to_frame().join(totals)

    totals['prob'] = totals['type totals'] / totals['totals'] * 100
    print(totals)  # FOR TESTING ONLY!! DELETE ME!!!

    return


if __name__ == '__main__':
    main()
