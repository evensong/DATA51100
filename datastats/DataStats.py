# Ben Haws 9/27/21
# Data51100 Fall 2021
# Programming Assignment #5

import numpy as np
import pandas as pd
import re


def get_start_time(x):
    if pd.isna(x):
        return 0
    else:
        return int(re.findall(r'[1-9]', x)[0])


# pulls public school information, selects columns and computes summary stats
def main():
    intro = 'DATA51100 - Fall 2021\nName: Ben Haws\nPROGRAMMING ASSIGNMENT #5'
    print(intro)

    # get data from .csv file
    schools = pd.read_csv('cps.csv')

    # create trimmed dataframe for output--our working frame
    cols = ['School_ID', 'Short_Name', 'Is_High_School', 'Zip',
            'Student_Count_Total', 'College_Enrollment_Rate_School']
    school_stats = schools[cols].copy()

    # isolate data about grades to populate lowest and highes grade col
    grades = schools['Grades_Offered_All']

    # here we get the lowest grades by taking the first element in all grades
    lowest = 'Lowest Grade'
    min_grades = pd.Series([x.split(',')[0] for x in grades])
    school_stats[lowest] = min_grades

    # get highest grade by taking the last element of each list in all grades
    max_grades = pd.Series([x.split(',')[-1] for x in grades])
    school_stats['Highest Grade'] = max_grades

    # parse times to get starting hours
    hours = schools['School_Hours']
    get_start_times = np.vectorize(get_start_time, otypes=[np.int64])
    school_stats['School_Start_Hour'] = get_start_times(hours)

    # Aggregate high school and non highschool data
    college = schools.loc[schools['Is_GoCPS_High_School']]['College_Enrollment_Rate_School']
    nhs_students = schools.loc[~schools['Is_GoCPS_High_School']]['Student_Count_Total']

    # Calculate means and stds
    mean_college = college.mean(skipna=True)
    std_college = college.std(skipna=True)
    mean_nhs = nhs_students.mean(skipna=True)
    std_nhs = nhs_students.std(skipna=True)

    # Aggregate start times and count
    start_dist = school_stats['School_Start_Hour'].value_counts()

    # mask schools not in the loop and count
    zip = school_stats['Zip']
    mask = ((zip != 60601) & (zip != 60602) & (zip != 60603) & (zip != 60604) &
            (zip != 60605) & (zip != 60606) & (zip != 60607) & (zip != 60616))
    out_of_loop = zip[mask].count()
    # Print data and stats, not required to exactly match example output
    print(school_stats.head(10))
    print('\nCollege Enrollment Rate for High Schools = ',
          '{0:.2f}'.format(mean_college), ' (std = ', '{0:.2f}'.format(std_college), ')')

    print('\nTota Student Count for non-High Schools = ',
          '{0:.2f}'.format(mean_nhs), ' (std = ', '{0:.2f}'.format(std_nhs), ')\n')
    print('Distribution of Starting Hours:\n\n8am: ',
          start_dist[8], '\n7am: ', start_dist[7], '\n9am: ', start_dist[9])

    print('\nNumber of schools outside loop: ', out_of_loop)
    return


if __name__ == '__main__':
    main()
