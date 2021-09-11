#K-Means Clustering, progrramming assignment 2 for DATA51100 Fall 2021

def floatable(s):
    'Determine if an object can be converted to type float'
    try: float(s)
    except ValueError: return False
    return True




def main():
    intro = 'DATA-51100, Spring 2021 \nNAME: Ben Haws\nPROGRAMMING ASSIGNMENT #2\n'
    print(intro)

    # get data from import file
    with open('input.txt') as infile:
        data = [float(x.rstrip()) for x in infile if floatable(x)]

    k = input('Enter the number of clusters: ')
    #user inputs cluster number k, program exits if noninteger is entered
    try: k = int(k)
    except ValueError: print(k + ' is not a valid input'); return
    if k > len(data): print('Error: k cannot exceed the number of data points'); return

    # set centroids--note that centroids are the first k elements of input.txt, not random assignment
    centroids = dict(zip(range(k), data[0:k]))

    #initialize dict for clusters: one empty list per value fro 0-k
    clusters = dict(zip(range(k), [] for x in range(k)))
    return
if __name__ == '__main__':
    main()
