import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

class ScoreParam:
    """The parameters for an alignment scoring function"""
    def __init__(self, gap, match, mismatch):
        self.gap = gap
        self.match = match
        self.mismatch = mismatch
def blast(x,y,g=-7,m=10,mm=-5):
    '''Make a balst matrix
    returns max score, location, and alignment matrix
    '''
    A = [[0]*(len(y)+1) for i in range(0,len(x)+1)]
    score=ScoreParam(g, m, mm)
    """Do a local alignment between x and y"""
    # create a zero-filled matrix
    best = 0
    optloc = (0,0)

    # fill in A in the right order
    for i in range(1, len(x)+1): # row [11]
        for j in range(1, len(y)+1): # column [33]
            # the local alignment recurrance rule:
            try:

                A[i][j] = max(A[i][j-1] + score.gap,# left
                              A[i-1][j] + score.gap,# bottom
                              A[i-1][j-1] + (score.match if x[i-1] == y[j-1] else score.mismatch),#left diagonal
                              0)

                # track the cell with the largest score
                if A[i][j] >= best:
                    best = A[i][j]
                    optloc = (i,j)
            except:
                e = None
                print('%i:%i'%(i,j))
    # return the opt score and the best location
    df = pd.DataFrame(A)
    return best, optloc, A, df
def trace(a,b,d):
    '''Finds indacies of max alignment scores'''
    r = b[0]
    c = b[1]
    ind = [b]
    # up top, up left, same left
    while [d[r-1][c],d[r-1][c-1], d[r][c-1]] != [0,0,0]:
        # take a step if the values are what we desire
        #index
        #up top
        ut = d[r-1][c]
        ul = d[r-1][c-1]
        sl = d[r][c-1]
        m = max([ut,ul,sl])
        if ut == m:
            ind.append((r-1,c))
            r-=1
        elif ul ==m:
            ind.append((r-1,c-1))
            r-=1
            c-=1
        elif sl==m:
            ind.append((r,c-1))
            c-=1
    return ind[::-1]
def as_string(ind,f,s):
    '''returns value of indacies as optimal substring alignments'''
    al1 = ''
    al2 = ''
    for i in ind:
        al1+=str(f[i[0]-1])
    for i in ind:
        al2+=str(s[i[1]-1])
    return al1,al2

## example usage
# s1="Go Dog Go!"
# s2="xxxxGo Dog Goxxx"
# a,b,c,d = blast(s1,s2)
# al1,al2 = as_string(trace(a,b,c),s1,s2)

## to make a heat map
# sns.heatmap(d,cmap="Blues")
# plt.xlabel("String 2")
# plt.ylabel("String 1")
# # plt.axis('off')
# plt.savefig(path)
