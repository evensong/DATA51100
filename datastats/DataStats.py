# Ben Haws 9/27/21
# Data51100 Fall 2021
# Programming Assignment #5

import pandas as pd
from pandas import DataFrame


# pulls public school information, selects columns and computes summary stats
def main():
    intro = 'DATA51100 - Fall 2021\nName: Ben Haws\nPROGRAMMING ASSIGNMENT #5'
    print(intro)

    # get data from .csv file
    schools = pd.read_csv('cps.csv')

    # create trimmed dataframe for output--our working frame
    cols = ['School_ID', 'Short_Name', 'Is_High_School', 'Zip',
            'Student_Count_Total', 'College_Enrollment_Rate_School']
    school_stats = schools[cols]

    # isolate data about grades to populate lowest and highes grade col
    grades = schools['Grades_Offered_All']

    # here we get the lowest grades by taking the first element in all grades
    min_grade = 'Lowest Grade Offered'
    school_stats[min_grade] = [x[0] for x in grades]
    school_stats[min_grade] = school_stats[min_grade].str.replace('P', 'PK')

    # get highest grade by taking the last element of each list in all grades
    school_stats['Highest Grade Offered'] = [x[len(x) - 1] for x in grades]

    # parse times to get starting and ending hours
    hours = schools['School_Hours']
    hours = hours.str.split('-', expand=True)
    hours = hours.drop(list(range(2, 5)), axis=1)

    print(school_stats.head(10))
    return


if __name__ == '__main__':
    main()
